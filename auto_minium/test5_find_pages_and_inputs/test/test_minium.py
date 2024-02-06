import minium

class minium_query(minium.MiniTest):
    def __init__(self, mini):
        super().__init__()
        self.mini = mini
    
    def get_pages(self, pages):
        self.pages = pages

    def test_get_sysyem_info(self):
        sys_info = self.mini.get_system_info()
        self.assertIn("SDKVersion", sys_info)