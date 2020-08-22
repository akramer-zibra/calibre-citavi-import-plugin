
from PyQt5.Qt import QWizardPage, QVBoxLayout, QLabel, QFileDialog

class FilepickPage(QWizardPage):

  @staticmethod
  def create(db):

    # Create a fresh wizard page
    page = QWizardPage()

    # TEST content
    l = QVBoxLayout()
    page.setLayout(l)

    label = QLabel('Wählen Sie hier die zu importierende BibTeX-Datei aus')
    l.addWidget(label)

    # Defines Filepicker for import file
    import_file = QFileDialog()
    import_file.setNameFilter("Files (*.bib)") # Only allow .bib files to be loaded
    l.addWidget(import_file)

    return page    
