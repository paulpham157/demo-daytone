# demo-daytone

## Yêu cầu phải có python hoặc nodejs, e viết đoạn python, các bác mà dùng node thì ném file demo.py vào chatGPT bảo nó convert sang nodejs cho

## Bước 1: Vào đây tạo acc: https://app.daytona.io/

## Bước 2: Đăng nhập, vào billing, add thẻ, BIN cũng đc: https://app.daytona.io/dashboard/billing

## Bước 3: Vào settings, copy organization id, lưu lại, tý dùng: https://app.daytona.io/dashboard/settings

## Bước 4: Vào keys, tạo 1 key, đặt tên gì cũng đc, copy lưu lại: https://app.daytona.io/dashboard/keys

## Bước 5: Link húp, điền lung tung, miễn là email khớp với email đăng ký, đoạn dùng bao nhiêu giờ mỗi tháng cứ để max: https://docs.google.com/forms/d/e/1FAIpQLScEj8D_QdhLKoOpPj51QuATLPnfGeG3LWd3-m5pEElLwM6Yyg

## Bước 6: Clone repo này về, hoặc download zip về cũng đc: https://github.com/paulpham157/demo-daytone

## Bước 7: Chui vào trong folder demo-daytona, cài đặt thư viện, hoặc nếu dùng node thì bảo GPT các thư viện cần thiết bên ấy:

```bash
pip install -r requirements.txt
```

## Bước 8: Copy file env.example và đổi tên thành .env

```bash
cp env.example .env
```

## Bước 9: Điền thông tin xác thực gồm key và organization vừa nãy vào .env

## Bước 10: Chạy file demo.py lên, chờ mấy giây thế là xong

```bash
python demo.py
```

## Bước 11: Mở trình duyệt lên, vào sandbox: https://app.daytona.io/dashboard/sandboxes

## Bước 12: Nhấn vào cái hình terminal ở cột "Access"

## Bước 13: Cài gì thì cài, chạy gì thì chạy. Use at your own risk!

## Check số tài nguyên giới hạn ở đây: https://app.daytona.io/dashboard/usage