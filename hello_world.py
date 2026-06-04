# { "Depends": "py-genlayer:test" }
from genlayer import *


class Greeting(gl.Contract):
    # Biến trạng thái lưu on-chain — phải khai báo trong thân class kèm kiểu dữ liệu
    message: str

    def __init__(self):
        # Chạy một lần khi contract được deploy
        self.message = "Hello from GenLayer testnet!"

    @gl.public.view
    def get_message(self) -> str:
        # Chỉ đọc, không đổi trạng thái
        return self.message

    @gl.public.write
    def set_message(self, new_message: str):
        # Ghi: cập nhật câu chào lưu trên chain
        self.message = new_message
