# GenLayer Testnet Playground

Các thử nghiệm của mình khi khám phá [GenLayer](https://genlayer.com) — một blockchain
nơi validator dùng LLM để chạy "Intelligent Contracts" (hợp đồng thông minh tích hợp AI)
viết bằng Python thay vì Solidity.

## Nội dung repo

- `hello_world.py` — một Intelligent Contract tối giản: lưu một câu chào on-chain,
  cho phép đọc và cập nhật lại. Viết bằng GenVM SDK (`from genlayer import *`).

## GenLayer là gì

Khác với smart contract truyền thống chỉ chạy code xác định (deterministic), Intelligent
Contract của GenLayer có thể hiểu ngôn ngữ tự nhiên, lấy dữ liệu web thời gian thực, và
đạt đồng thuận qua nhiều mô hình AI (cơ chế "Optimistic Democracy").

## Chạy thử

Có thể deploy và test contract ngay trên trình duyệt bằng
[GenLayer Studio](https://studio.genlayer.com) — không cần cài đặt gì ở máy.

## Links

- Docs: https://docs.genlayer.com
- Studio: https://studio.genlayer.com
- Testnet: Bradbury
