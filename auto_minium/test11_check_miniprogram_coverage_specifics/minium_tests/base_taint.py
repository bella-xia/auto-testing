import minium_tests.base_case as base_case
import minium, json
from collections import namedtuple
from typing import Dict, List

'''
PS: selector 仅支持下列语法:

ID选择器: #the-id
class选择器(可以连续指定多个): .a-class.another-class
标签选择器: view
子元素选择器: .the-parent > .the-child
后代选择器: .the-ancestor .the-descendant
跨自定义组件的后代选择器: custom-element1>>>.custom-element2>>>.the-descendant
custom-element1 和 .custom-element2必须是自定义组件标签或者能获取到自定义组件的选择器
多选择器的并集：#a-node, .some-other-nodes
xpath: 可以在真机调试的wxml pannel选择节点->右键->copy->copy full xpath获取，暂不支持[text()='xxx']这类xpath条件
'''
SelectorInfo = namedtuple('SelectorInfo', ['selector', 'inner_text', 'text_contains', 'value'])

class BaseTaint(base_case.BaseCase):
    """
    封装公用页面基础操作方法
    """
    
    def get_element_using_selector(self, selector_info):
        return self.page.get_element(
            selector=selector_info.selector, 
            inner_text=selector_info.inner_text, 
            text_contains=selector_info.text_contains, 
            value=selector_info.value)

    def get_json_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = file.read()
        return json.loads(json_data)

    def input_text_helper(self, default_text, class_name):
        POTENTIAL_IDENTIFIER_AND_INPUT = {'电话' : '13880000000',
                                          '手机':'13880000000',
                                          'phone':'13880000000',
                                          'mobile':'13880000000',
                                          '邮箱': 'string_sample@163.com',
                                           'email':'string_sample@163.com'}
        for (ident, input_text) in POTENTIAL_IDENTIFIER_AND_INPUT.items():
            if (class_name.lower()).find(ident) != -1:
                return input_text
        return default_text

    def hook_wx_methods_with_formelement_binds(
        self,
        element: minium.BaseElement,
        input_text: str,
        wx_methods: List[str],
        is_form: bool = False
    ) -> Dict[str, any]:
        """
        this function hoods a method used by a form via bindsubmit

        Args:
        ele (minium.BaseElement) : the element of interest
        input_text (str) : the text inputed to each block of the form
        wx_methods (list[str]): the list of wx methods to be tested
        is_form (bool) : identifier for whether this is a form element or input element

        Returns:
        Dict[str, any]: a dictionary of all the instances where an arg 
        passes into the wx api method
        """
        callback_arr = {}
        return_arr = {}
        for wx_method in wx_methods:
            callback_arr[wx_method] = minium.Callback()
            self.app.hook_wx_method(
                wx_method, callback=callback_arr[wx_method].callback
            )

        if is_form:
            all_inputs = element.get_elements("input")
            input_args = {}
            if len(all_inputs) == 0:
                print("unable to find any input. Submit attempt failed")
            else:
                print(f"the current form has {len(all_inputs)} fields")
                for input_ele in all_inputs:
                    class_name = input_ele.attribute("name")[0]
                    input_args[class_name] = self.input_text_helper(input_text, class_name)
            print(f'here is the input argumets: {input_args}')
            element.trigger("submit", {"value": input_args})
        else:
            element.trigger('change', {'value': input_text})

        for wx_method in wx_methods:
            if callback_arr[wx_method].wait_called(timeout=5) is True:
                return_arr[wx_method] = callback_arr[wx_method].get_callback_result()
            else:
                return_arr[wx_method] = None
            self.app.release_hook_wx_method(wx_method)

        return return_arr

    def hook_wx_methods_with_element_tap(
        self,
        element: minium.BaseElement,
        wx_methods: List[str]
    ) -> Dict[str, any]:

        callback_arr = {}
        return_arr = {}
        for wx_method in wx_methods:
            callback_arr[wx_method] = minium.Callback()
            self.app.hook_wx_method(wx_method, 
                                    callback=callback_arr[wx_method])

        element.tap()

        for wx_method in wx_methods:
            if callback_arr[wx_method].wait_called(timeout=10) is True:
                return_arr[wx_method] = callback_arr[wx_method].get_callback_result()
            else:
                return_arr[wx_method] = None
            self.app.release_hook_wx_method(wx_method)

        return return_arr

    def hook_wx_methods_with_page_defined_method_call(
        self, page: str, wx_methods: List[str], page_defined_method: str,
        method_args: Dict[str, any]
    ) -> Dict[str, any]:
        
        if (self.app.get_current_page() != page):
            print(f"currently at page {self.app.get_current_page()}, redirecting to {page}")
            self.open_route("/" + page)
        
        callback_arr = {}
        return_arr = {}
        for wx_method in wx_methods:
            callback_arr[wx_method] = minium.Callback()
            self.app.hook_wx_method(wx_method, callback=callback_arr[wx_method])

        self.app.current_page.call_method(page_defined_method, [method_args])

        for wx_method in wx_methods:
            if callback_arr[wx_method].wait_called(timeout=10) is True:
                return_arr[wx_method] = callback_arr[wx_method].get_callback_result()
            else:
                return_arr[wx_method] = None
            self.app.release_hook_wx_method(wx_method)

        return return_arr
    
    def hook_wx_methods_with_open_page(
        self, page: str, wx_methods: List[str]
    ) -> Dict[str, any]:
        
        if (self.app.get_current_page() != page):
            print(f"currently at page {self.app.get_current_page()}, redirecting to {page}")
            self.open_route("/" + page)
        
        callback_arr = {}
        return_arr = {}
        for wx_method in wx_methods:
            callback_arr[wx_method] = minium.Callback()
            self.app.hook_wx_method(wx_method, callback=callback_arr[wx_method])

        self.open_route("/" + page)

        for wx_method in wx_methods:
            if callback_arr[wx_method].wait_called(timeout=10) is True:
                return_arr[wx_method] = callback_arr[wx_method].get_callback_result()
            else:
                return_arr[wx_method] = None
            self.app.release_hook_wx_method(wx_method)

        return return_arr