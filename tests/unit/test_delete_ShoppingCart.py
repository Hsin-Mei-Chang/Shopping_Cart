import unittest
from shopping.shoppingCart import ShoppingCart
class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        # 設置測試環境，創建一個購物車對象並加入一些商品
        self.cart = ShoppingCart()
        self.cart.add_to_cart(1)  # 商品1加入購物車
        self.cart.add_to_cart(2)  # 商品2加入購物車

    def test_delete_to_cart_valid(self):
        # 測試刪除存在於購物車中的商品
        self.cart.delete_to_cart(1)
        self.assertEqual(len(self.cart.shopping_cart), 1)  # 應該只剩下商品2
        self.assertNotIn({"id": 1, **self.cart.products[1]}, self.cart.shopping_cart)  # 應該不再包含商品1

    def test_delete_to_cart_invalid(self):
        # 測試刪除不在購物車中的商品
        self.cart.delete_to_cart(3)  # 商品3不在購物車中
        self.assertEqual(len(self.cart.shopping_cart), 2)  # 購物車內容不應改變
        self.assertIn({"id": 1, **self.cart.products[1]}, self.cart.shopping_cart)  # 商品1仍在購物車中
        self.assertIn({"id": 2, **self.cart.products[2]}, self.cart.shopping_cart)  # 商品2仍在購物車中

    def test_delete_from_empty_cart(self):
        # 測試從空購物車刪除商品
        empty_cart = ShoppingCart()  # 創建一個空購物車
        empty_cart.delete_to_cart(1)  # 嘗試刪除商品1
        self.assertEqual(len(empty_cart.shopping_cart), 0)  # 購物車仍為空
        # 應該顯示商品不在購物車內的錯誤訊息
        # 注意：這裡是無法直接捕捉 print 輸出的，因此我們不會在這個測試中檢查錯誤訊息

    def tearDown(self):
        # 測試後清理環境
        pass

if __name__ == '__main__':
    unittest.main()
