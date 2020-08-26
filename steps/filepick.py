from PyQt5.Qt import QWizardPage, QVBoxLayout, QLabel, QFileDialog, QDialog

# Import logging code
from calibre import prints
from calibre.utils.monotonic import monotonic

class FilepickStep():

  __create_key = object()

  """ Protected constructor method """
  def __init__(self, create_key, parent, db):
    assert(create_key == FilepickStep.__create_key), \
        "FilepickStep objects must be created using FilepickStep.build"
    
    # Dependency injection
    self.parent = parent
    self.db = db

    # Defines Filepicker for import file
    self.import_file = QFileDialog()
    self.import_file.setNameFilter("Files (*.bib)") # Only allow .bib files to be loaded

    if self.import_file.exec_() == QDialog.Accepted:
      filename = self.import_file.selectedFiles()
    if filename:
      self.process(str(filename[0]))      

  """ Method processes the selected import file """
  def process(self, url):
    prints(url)

  ''' Factory Method for this page '''
  @classmethod
  def build(cls, parent, db):
      return FilepickStep(cls.__create_key, parent, db)