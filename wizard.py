
from PyQt5.Qt import QWizard

from calibre_plugins.citavi_import_plugin.steps.filepick import FilepickStep

class ImportWizard(QWizard): 

  def __init__(self, gui, icon, do_user_config):

    QWizard.__init__(self, gui)
    self.gui = gui
    self.do_user_config = do_user_config

    # Cache db reference
    self.db = gui.current_db

    # Configure wizard window
    self.setWindowTitle('Citavi Import Plugin')    
    
    # Define wizard with its pages
    # AND pass calibre config and db to this pages
    self.addPage(FilepickPage.build(self, self.db))
       


