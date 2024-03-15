import minium

class TestInput(minium.MiniTest):
    
    def open_route(self, route):
        try:
            self.app.navigate_to(route)
        except Exception as e:
            exception_message = e.args[0] if e.args else str(e)
            if (exception_message == "can not navigateTo a tabbar page"):
                self.app.switch_tab(route)
            else:
                print(f'having exception {exception_message} on navigating to page {route}')
            
    def try_input(self, input_ele, text):
        input_ele.input(text)
    
    def try_input_through_trigger(self, input_ele, text):
        input_ele.trigger("change", {"value": text})
    
    def find_all_pages(self):
        all_pages_path = self.app.get_all_pages_path()
        return all_pages_path

    def find_all_inputs(self):
        all_inputs = self.page.get_elements("input")
        return all_inputs
    
    def find_class(self, class_name, duplicates=False):
        if duplicates:
            class_eles = self.page.get_elements(class_name)
            return class_eles
        else:
            class_ele = self.page.get_element(class_name)
            return class_ele
    
    def not_test_inputs(self):
        pages = self.find_all_pages()
        for page in pages:
            self.open_route("/" + page)
            self.page.wait_for(5)
            self.app.navigate_back()
    
    def check_input(self, input_text, expected_input):
        try: 
            self.assertEqual(expected_input, input_text, f"element is properly modified")
        except AssertionError:
            print(f"failed assertion, expected input {expected_input}, but gets {input_text}")
    
    def test_make_and_check_input(self):
        edit_page_name = "/pages/editPersonInfo/editPersonInfo"
        storage_page_name = "pages/personInfo/personInfo"

        self.open_route(edit_page_name)
        inputs = self.find_all_inputs()
        for input_box in inputs:
            self.try_input_through_trigger(input_box, "string")
        btn_ele = self.find_class(".edit-btn")
        btn_ele.click()
        self.page.wait_for(10)
        cur_page = self.app.get_current_page()
        self.assertEqual(cur_page, storage_page_name, "check if the miniprogram navigates back to the page")
        all_textboxes = self.find_class(".cell-ft", duplicates=True)
        for textbox in all_textboxes:
            self.check_input(textbox.text, "string")

    def tearDown(self):
        self.mini.shutdown()
        super().tearDown()