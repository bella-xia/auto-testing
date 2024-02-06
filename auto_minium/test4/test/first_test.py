import minium

class FirstTest(minium.MiniTest):
    def test_get_sysyem_info(self):
        sys_info = self.mini.get_system_info()
        self.assertIn("SDKVersion", sys_info)