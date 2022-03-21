#declare character  used by this game
define tp = Character("Thuyền phó")

label start:
    scene ship16 with fade
    menu:
        "Cho Arashi tiếp tục đuổi theo":
            jump b1

label b1:
    scene ship8 with fade
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":
            jump b2
        "Sau khi Tomohaga hạ cánh":
            jump Tomohaga1
label Tomohaga1:
    scene plane13 with fade
    menu:
        "Tấn công hạm đội đối phương ngay lập tức":
            jump b2
        "Tấn công Midway":
            jump b2
label b2:
    scene plane7 with fade
    menu:
        "Dừng việc phóng máy bay, chuẩn bị súng phòng không":
            jump c1
label c1:
    scene plane15 with fade
    menu:
        "Báo cáo tình hình":
            jump c2
label c2:
    scene plane9 with fade
    menu:
        "Tiếp tục phóng máy bay tấn công":
            jump c3
label c3:
    scene plane8 with fade
    menu:
        "Dừng việc phóng máy bay và chuẩn bị súng phòng không":
            jump c4
label c4:
    scene plane9 with fade
    menu:
        "Báo cáo tình hình":
            jump c5
label c5:
    scene plane10 with fade
    menu:
        "Tiếp tục phóng máy bay tấn công":
            jump c6
label c6:
    scene plane11 with fade
    menu:
        "Gọi máy bay quay lại bảo vệ trên đầu":
            jump goi1
        "Để tất cả máy bay tập trung, tấn công máy bay của địch":
            jump goi1
label goi1:
    scene black with fade
    "0715!"
    scene plane4 with fade
    menu:
        "Tấn công bằng đội máy bay của Tomonaga": #0715 tấn công bằng đội máy bay của Tomonaga
            jump kk
        "Không tấn công bằng đội máy bay của Tomonaga":
            jump qq
label kk:
    scene plane6 with fade
    menu:
        "Báo cáo tình hình":
            jump bc1
label bc1:
    scene ship19 with fade
    menu:
        "Rút lui":
            jump rl1
        "Đuổi theo":
            jump dt1
label rl1:
    scene black with fade
    menu:
        "Ending 1 (fire)":
            jump endingfire1
label dt1:
    scene ship16 with fade
    menu:
        "Phản công":
            jump pc
label qq:
    scene ship19 with fade
    menu:
        "Báo cáo tình hình":
            jump bc2
label bc2:
    scene ship4 with fade
    menu:
        "Ngồi trên tàu (đang chìm) và đợi chết":
            jump ntt1
        "Tháo chạy bằng xuồng và chỉ huy tiếp từ tàu Nagara":
            jump ttt1
label ntt1:
    scene black with fade
    menu:
        "Ending 2 (die)":
            jump endingdie2
label ttt1:
    scene ship11 with fade
    menu:
        "Rút lui":
            jump mra
        "Đuổi theo":
            jump mrt
label mra:
    scene black with fade
    menu:
        "Ending 1 (fire)":
            jump endingfire1
label mrt:
    scene ship16 with fade
    menu:
        "Phản công":
            jump pc
label pc:
    scene ship17 with fade
    menu:
        "Rút lui":
            jump rl2
        "Tiếp tục tấn công":
            jump tttc2
label rl2:
    scene black with fade
    menu:
        "Ending 1 (fire)":
            jump endingfire1
label tttc2:
    scene plane with fade
    menu:
        "Đi hướng Tấy Bắc":
            jump dhtb1
        "Đi hướng Đông Nam":
            jump dhdn1
label dhtb1:
    scene black with fade
    menu:
        "Ending 3 (live&job)":
            jump endinglivejob3
label dhdn1:
    scene ship9 with fade
    menu:
        "Rẽ trái khẩn cấp":
            jump rtkc1
        "Đi thẳng tieps":
            jump dtt1
label rtkc1:
    scene plane11 with fade
    menu:
        "Báo cáo tình hình":
            jump bc3
label dtt1:
    scene plane11 with fade
    menu:
        "Báo cáo tình hình":
            jump bc3
label bc3:
    scene ship2 with fade
    menu:
        "Rút lui":
            jump rl3

label rl3:
    scene black with fade
    menu:
        "Ending 3 (live&job)":
            jump endinglivejob3
label endingfire1:
    scene biduoikhoiquandoi with fade
    tp "Bạn đã chính thức bị đuổi khỏi quân đội"
    tp "Ngày 14/8/1945, phát xít Nhật đầu hàng không điều kiện, kết thúc chiến tranh thế giới thứ hai"
label endingdie2:
    scene banzai with fade
    tp "Bạn đã hy sinh anh dũng trong trận chiến"
    tp "Ngày 14/8/1945, phát xít Nhật đầu hàng không điều kiện, kết thúc chiến tranh thế giới thứ hai"
label endinglivejob3:
    scene aschool with fade
    show giaosu2 at right:
    tp "Bạn đã sống sót trở về"
    tp "Sau khi Nhật Bản đầu hàng quân Đồng Minh, bạn được nhận vào, \"giảng dạy nghiên cứu ở 1 trường học\""
    show vogiaosu at right:
    tp "Bạn đã cưới 1 giáo viên trẻ cùng trường"
    show vogiaosu1 at right:
    tp "Chúc mừng, đó là 1 cô gái nóng bỏng"
    show giaosu1 at right:
    tp "Bạn có cuộc sống viên mãn và hạnh phúc"

#this is the end of the game
    return
