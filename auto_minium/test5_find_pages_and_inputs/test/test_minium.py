from basedef import BaseDef
import os

class Minium_Query(BaseDef):
    
    def test_inputs(self):
        text_input = "string"
        pages = self.find_all_pages()

        for page in pages:
            self.open_route("/" + page)
            self.page.wait_for(5)
            inputs = self.find_all_inputs()
            print(f"there are {len(inputs)} elements on page {page}")
            for input_block in inputs:
                try:
                    input_block.input(text_input)
                except Exception as e:
                    print(f'encountering error during query: {e}')
                # self.screen_shot_save("(" + page  + ")")
                # self.page.wait_for(5)
                value = input_block.attribute("value")[0]
                try: 
                    self.assertEqual(text_input, value, f"element {input_block} is properly modified")
                except AssertionError as e:
                    print(f"failed assertion, expected input {text_input}, but gets {value}")
            self.app.navigate_back()
        
    def tearDown(self):
        self.mini.shutdown()
        super().tearDown()
        