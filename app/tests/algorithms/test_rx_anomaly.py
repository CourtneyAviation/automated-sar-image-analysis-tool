from PyQt5.QtCore import Qt

def testRXAnomalyE2E(main_window, testData, qtbot):
    main_window.inputFolderLine.setText(testData['RGB_Input'])
    main_window.outputFolderLine.setText(testData['RGB_Output'])
    assert main_window.algorithmWidget is not None
    main_window.algorithmComboBox.setCurrentText('RX Anomaly')
    assert main_window.algorithmWidget is not None
    assert main_window.AdvancedFeaturesWidget.isVisible()
    algorithmWidget = main_window.algorithmWidget
    algorithmWidget.sensitivitySlider.setValue(7)
    algorithmWidget.segmentsComboBox.setCurrentText(str(2))
    assert main_window.startButton.isEnabled()
    assert not main_window.cancelButton.isEnabled()
    assert not main_window.viewResultsButton.isEnabled()
    qtbot.mouseClick(main_window.startButton, Qt.MouseButton.LeftButton)
    assert not main_window.startButton.isEnabled()
    assert main_window.cancelButton.isEnabled()
    assert not main_window.startButton.isEnabled()
    qtbot.waitUntil(lambda: main_window.viewResultsButton.isEnabled(), timeout=20000)
    assert main_window.startButton.isEnabled()
    assert not main_window.cancelButton.isEnabled()
    assert main_window.viewResultsButton.isEnabled()
    qtbot.mouseClick(main_window.viewResultsButton, Qt.MouseButton.LeftButton)
    assert main_window.viewer is not None
    viewer = main_window.viewer
    assert viewer.fileNameLabel.text() is not None
    assert viewer.images is not None
    assert len(viewer.images) is not 0
    assert viewer.mainImage is not None
    assert viewer.aoiListWidget is not None
    assert len(viewer.aoiListWidget) is not 0
    assert len(viewer.aoiListWidget) is not 0
    assert viewer.statusbar.currentMessage() is not ""
    qtbot.mouseClick(viewer.nextImageButton, Qt.MouseButton.LeftButton)
    assert viewer.fileNameLabel.text() is not None
    assert viewer.images is not None
    assert len(viewer.images) is not 0
    assert viewer.mainImage is not None
    assert viewer.aoiListWidget is not None
    assert len(viewer.aoiListWidget) is not 0
    assert len(viewer.aoiListWidget) is not 0
    assert viewer.statusbar.currentMessage() is not ""
    qtbot.mouseClick(viewer.previousImageButton, Qt.MouseButton.LeftButton)
    assert viewer.fileNameLabel.text() is not None
    assert viewer.images is not None
    assert len(viewer.images) is not 0
    assert viewer.mainImage is not None
    assert viewer.aoiListWidget is not None
    assert len(viewer.aoiListWidget) is not 0
    assert len(viewer.aoiListWidget) is not 0
    assert viewer.statusbar.currentMessage() is not ""
