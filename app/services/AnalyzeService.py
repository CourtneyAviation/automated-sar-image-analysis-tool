import functools

import numpy as np
import cv2
import os
import imghdr
import xml.etree.ElementTree as ET
import logging
import piexif
from services.HistogramNormalizationService import HistogramNormalizationService
from concurrent.futures import ProcessPoolExecutor
from helpers.ColorUtils import ColorUtils
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

"""****Import Algorithms****"""
from algorithms import *
"""****End Algorithm Import****"""

class AnalyzeService(QObject):

	#Signals to send info back to the GUI
	sig_msg = pyqtSignal(str)
	sig_done = pyqtSignal(int, int)

	def __init__(self, id,algorithm, input, output, identifierColor, min_area, num_threads, histogram_reference_path, options):
		super().__init__()
		self.algorithm = algorithm
		self.input = input
		self.output_dir = output
		self.output = os.path.join(output, "ADIAT_Results")
		self.identifierColor = identifierColor
		self.options = options
		self.min_area = min_area
		self.num_threads = num_threads
		self.hist_ref_path = histogram_reference_path
		self.__id = id
		self.images_with_aois = 0
	
	
	@pyqtSlot()
	def processFiles(self):
		try:
			self.setupOutputDir();
			self.setupOutputXml()

			histogram_service = None
			if self.hist_ref_path is not None:
				histogram_service = HistogramNormalizationService(self.hist_ref_path)
			#Create an instance of the algorithm class
			cls = globals()[self.algorithm+"Process"]
			instance = cls(self.identifierColor, self.min_area, self.options)
			
			#loop through all of the files in the input directory and process them in multiple threads
			with ProcessPoolExecutor(self.num_threads) as executor:
				for file in os.listdir(self.input):
					full_path =  os.path.join(self.input, file)
					if(os.path.isdir(full_path)):
						continue
					if imghdr.what(full_path) is not None:
						self.sig_msg.emit('Processing file: ' + file)
						future = executor.submit(AnalyzeService.processFile, instance, file, full_path, histogram_service)
						future.add_done_callback(functools.partial(self.processComplete, file, full_path))
						#self.processFile(instance, file, full_path)
					else:
						self.sig_msg.emit("Skipping "+file+ " - File is not an image")

			self.writeXmlFile()
			self.sig_done.emit(self.__id, self.images_with_aois)
		except Exception as e:
			logging.exception(e)

	@staticmethod
	def processFile(instance, file, full_path, histogram_service):
		img = cv2.imread(full_path)
		if histogram_service is not None:
			img = histogram_service.matchHistograms(img)
		try:
			return instance.processImage(img)
		except Exception as e:
			logging.exception(e)

	def processComplete(self, file, full_path, future):
		if future.done():
			exif_dict = piexif.load(full_path)
			exif_bytes = piexif.dump(exif_dict)

			result = future.result()[0]
			areas_of_interest = future.result()[1]
			if result is not None:
				output_file = self.output+"/"+file
				cv2.imwrite(output_file, result)
				self.addImageToXml(file,areas_of_interest)
				self.sig_msg.emit('Areas of interest identified in '+file)
				self.images_with_aois += 1
				piexif.insert(exif_bytes, output_file)
	def setupOutputDir(self):
		try:
			if(os.path.isdir(self.output)):
				for the_file in os.listdir(self.output):
				    file_path = os.path.join(self.output, the_file)
				    try:
				        if os.path.isfile(file_path):
				            os.unlink(file_path)
				        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
				    except Exception as e:
				        logging.exception(e)
			else:
				os.mkdir(self.output)
		except Exception as e:
			logging.exception(e)

	def setupOutputXml(self):
		try:
			self.xml = ET.Element('data')
			settings_xml = ET.SubElement(self.xml, "settings")
			settings_xml.set("input_dir", self.input)
			settings_xml.set("output_dir", self.output_dir)
			settings_xml.set("identifier_color", self.identifierColor)
			settings_xml.set("algorithm", self.algorithm)
			settings_xml.set("num_threads", str(self.num_threads))
			settings_xml.set("min_area", str(self.min_area))
			options_xml = ET.SubElement(settings_xml, "options")
			for key, value in self.options.items():
				option_xml = ET.SubElement(options_xml, "option")
				option_xml.set("name", key)
				option_xml.set("value", str(value))
			self.images_xml = ET.SubElement(self.xml, "images")
		except Exception as e:
			logging.exception(e)

	def addImageToXml(self, file, areas_of_interest):
		image = ET.SubElement(self.images_xml, 'image')
		image.set('file_name',file)
		for area in areas_of_interest:
			area_xml = ET.SubElement(image, 'areas_of_interest')
			area_xml.set('center', str(area['center']))
			area_xml.set('radius', str(area['radius']))
			area_xml.set('area', str(area['area']))


	def writeXmlFile(self):
		mydata = ET.ElementTree(self.xml)
		file_path = os.path.join(self.output, "ADIAT_Data.xml")
		with open(file_path, "wb") as fh:
			mydata.write(fh)