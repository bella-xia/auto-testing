import minium

class FirstTest(minium.MiniTest):

    def test_search(self):
        '''
        turn human operation to auto-operation

        1. 梳理业务流程
        2. 业务流程抽象 - 伪代码

        测试搜索功能：
        1. 判断页面是否有搜索输入框
        2. 搜索是否展示搜索结果
        3. 点击取消是否恢复原样
        '''

        # 1. 存在输入框 [自动化定位]
        searchInputExists = self.page.element_is_exists("input[placeholder='iphone 13 火热发售中']")
        self.assertTrue(searchInputExists, "首页是否存在输入框")

        # 2. 进行搜索
        searchInput = self.page.get_element("input[placeholder='iphone 13 火热发售中']")

        #searchInputBoundingBoxExists = self.page.element_is_exists("view[class='t-class-input-container']")
        #self.assertTrue(searchInputBoundingBoxExists , "首页是否存在输入框 view")
        # 点击输入框
        searchInput.tap(force=True)

        # 等待搜索结果
        self.page.wait_for(5)

        # 输入，进行搜索 【输入 + 搜索】
        itemListExists = self.page.element_is_exists("view[data-index='1']")
        self.assertTrue(itemListExists, "点击是否存在历史记录")

        itemList = self.page.get_element("view[data-index='1']")
        itemList.tap()

        # 等待搜索结果
        self.page.wait_for(5)

        # 3. 写断言：用代码检查是否存在搜索结果
        searchResultExists = self.page.element_is_exists("view['.goods-card__body']")
        self.assertTrue(searchResultExists, "用户搜索后是否弹出搜索结果")

        # 4. 点击取消

        # 5. 写断言：是否恢复原样