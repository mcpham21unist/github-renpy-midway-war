define tp = Character("Phó Chỉ Huy", color="c8ffc8")
define noti = Character("Thông Báo", color="9FE2BF")
define dmr = Character("Damage Report", color="FF7F50")

#The game start here

label start: #(0430) đô đốc phóng máy bay về phía trước
    "0430!"
    scene phongdochoi with fade:
        size(1300,720)
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc, theo như kế hoạch, bây giờ chúng ta phải phóng\"các máy bay trinh thám để quan sát mặt trận phía trước\""
    menu:
        "Ra lệnh cho máy bay trinh thám":
            jump a3
        "Chúng ta không cần máy bay trinh thám":
            jump a2

label a3: #Ra lệnh cho máy bay trinh thám
    scene plane2 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc, hãy cho máy bay tấn công hải quân Hoa Kì ở Midway nhưu theo kế hoạch"
    menu:
        "không phải bây giờ":  #####################
            "Đây là thời điểm tấn công theo kế hoạch, thời tiết thuận lợi\"và máy bay đủ tầm, các phi công đều đã chuẩn bị\""
            jump a4
        "Tân công Midway":     #####################
            "Nếu chúng ta trì hoãn sự tấn công, thì đối phương sẽ có thêm thời gian\chuẩn bị hoặc còn có thể phản công, thời tiết có thể trở nên xấu đi\""
            jump a5

label a2: # Chúng ta không cần máy bay trinh thám (random)
    menu:
        "Ending 2 (die)":
            jump ending2

label a4: # không phải bây giờ (random)
    menu:
        "Ending 1(fire)":
            jump ending1

label a5: # tấn công Midway
    scene plane3 with fade
    "Tuyệt vời, đội máy bay tấn công Midway sẽ có phi công Tomonaga dẫn đầu."
    "Với anh ta, chúng ta có thể yên tâm là Midway sẽ bị vô hiệu hóa."
    "Hãy chúc các phi công trẻ của chúng ta trở lại an toàn."
    scene black with fade
    "0500!"
    scene plane with fade
    "Thông báo! Máy bay trinh thám Tone 4 vì sự cố kĩ thuật đã bị phóng muộn mất 30 phút."
    scene black with fade
    "0532!"
    scene ship8 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc! Một máy bay Mĩ Catalina PBY đã phát hiện\ra hạm đội của chúng ta. Chúng ta đã mất yếu tố bất ngờ\""
    tp "Tệ hơn nữa, máy bay thả bom của chúng ta chưa đến đảo Midway,\có nghĩa là máy bay Mĩ ở đảo Midway có thể tấn công hạm đội của t bất cứ lúc nào.\""
    tp "Chúng ta phải làm sao đây"
    menu:
        "Không cho thêm máy bay bảo vệ":    ##########################
        "Chúng ta đã có nhiều máy bay đang bay trên đầu để bảo vệ hạm đội.\Hơn nữa, đối phương không thể phản ứng nhanh đến thế được, chúng ta sẽ có thừa thời gian để chuẩn bị một khi phát hiện máy bay địch\""
            jump a6
        "Cho thêm máy bay bảo vệ":          ##########################
        "Có càng nhiều máy bay bảo vệ hạm đội càng an toàn,\ nhưng phải dùng các máy bay dự trữ, chúng ta sẽ không sẵn sàng nếu phát hiện hạm đội đối phương\""
            jump a7
label a6: # "0532" cho máy bay bảo vệ trước khi bị tấn công
    "0700!"
    scene ship10 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Báo cáo! Có 1 máy bay ném bom đang tiến tới tàu của chúng ta."
    tp "Không thể nào"
    tp "Máy bay đó đang cháy, mà vẫn nhắm tới chúng ta."
    tp "Cúi đầu xuống!"
    "Bọn Mĩ không thể dũng cảm như thế này được"
    "Chắc chắn là do bộ điều khiển của nó đã bị hỏng"
    "Cái máy bay đó đã đâm trượt tàu của mình, nhưng vài thủy thủ đã bị thương\ Họ đã được đưa đến phòng y tế.\""
    tp "Đô đốc! Phi công Tomonaga sau khi tấn công Midway báo rằng\chúng ta cần 1 đợt tấn công nữa mới vô hiệu hóa được hòn đảo.\""
    tp "Hơn nữa, máy bay địch đang tiến tới hạm đội"
    menu:
        "Phóng máy bay bảo vệ":                            #############################
        "Đây là một hành động rất nguy hiểm, khi đang bị tấn công, tàu sân bay không thể phóng thêm máy bay mới"
        "Rõ, tôi chúc đô đốc may mắn cho cuộc tấn công sắp tới"
            jump a9
        "Không phóng thêm máy bay, tập trung né":          #############################
        "Khi đang bị tấn công, các tàu sân bay tuyệt đối không được phóng máy bay mới, vì điều này sẽ làm giảm sự cơ động của tàu sân bay, và khiến tàu sân bay dễ bị cháy nổ hơn"
            jump a8
label a7: # "0532" ko cho thêm máy bay bảo vệ trước khi bị tấn công
    "0700!"
    scene ship10 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc! Phi công Tomonaga sau khi tấn công Midway báo rằng\chúng ta cần 1 đợt tấn công nữa mới vô hiệu hóa được hòn đảo.\""
    tp "Hơn nữa, máy bay địch đang tiến tới hạm đội"
    menu:
        "Phóng máy bay bảo vệ":                            #############################
        "Đây là một hành động rất nguy hiểm, khi đang bị tấn công, tàu sân bay không thể phóng thêm máy bay mới"
        "Rõ, tôi chúc đô đốc may mắn cho cuộc tấn công sắp tới"
            jump a9
        "Không phóng thêm máy bay, tập trung né":          #############################
        "Khi đang bị tấn công, các tàu sân bay tuyệt đối không được phóng máy bay mới, vì điều này sẽ làm giảm sự cơ động của tàu sân bay, và khiến tàu sân bay dễ bị cháy nổ hơn"
            jump a8

label a9: # "0700" phóng máy bay bảo vệ
    menu:
        "Ending 4 (die)":
            jump ending4
label a8: # "0700" né máy bay địch, không phóng máy bay ta (lần 1)
    "0700!"
    scene deakagi1 with fade
    menu:
        "Né máy bay địch không phóng máy bay ta":
        jump a10
label a10: # "Some time later" sử dụng súng phòng không lần 1
    "Some time later"
    scene deakagi2 with fade
    show thuyenpho at right:
            size(450,720)
        tp "Cẩn thận đô đốc! 4 máy bay thả ngư lôi đang ở bên phía cảng"
        menu:
            "Sử dụng súng phòng không":
                jump a11
label a11: # Sử dụng súng phòng không lần 2
    scene atakagi1 with fade
    menu:
        "Sử dụng súng phòng không lần 2":
            jump a12
label a12: # Báo cáo tình hình chiến dịch đợt 1
    scene phongdochoi with fade:
        size(1300,720)
    dmr "Chúng ta đã mất 2 máy bay Zero"
    dmr "Các con tàu còn lại"
    dmr "Trên bầu trời đã hết máy bay địch, cuộc tấn công của địch đã kết thúc."
    dmr "Và đến bây giờ vẫn chưa có thông báo gì từ máy bay trinh thám."
    scene black with fade
    "0715!"
    scene phongdochoi with fade:
        size(1300,720)
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc, tiện thể đang trong thời gian an toàn, ngài cần trả lời yêu cầu của Tomonaga\Chúng ta cần 1 đợt nữa mới phá hủy được sân bay ở Midway.\""
    menu:
        "Tấn công bằng đội máy bay của Tomonaga":
        "Đợi đội máy bay của Tomonaga quay trở lại, tiếp nhiên liệu và vũ khí, rồi quay lại tấn công"
        "Lựa chọn này sẽ tốn rất nhiều thời gian, quân Mĩ có thể\sửa lại sân bay và chuẩn bị phòng thủ, sẽ dẫn đến thêm mạng chết\""
        "Rõ"
            jump a62
        "Tấn công bằng máy bay dữ trữ":
        "Các máy bay thả ngư lôi dự trữ sẽ thay vũ khí để thả bom. Những máy bay này đang không làm gì"
        "Nhưng mình sẽ không có máy bay dự bị trong trường hợp phát hiện tàu sân bay địch"
        "Máy bay vừa nãy suýt đâm vào tàu chứng minh rằng midway vẫn là mối đe dọa"
        "Rõ"
            jump a13

# Bắt đầu từ chỗ này sẽ phân tách thành 2 nhánh lớn
# 1 nhánh là a13
# 1 nhánh là a62
# dài vcl thề



label a13: # "0715" tấn công bằng máy bay dự trữ
    scene plane13 with fade
    "Thay đổi các máy bay thả ngư lôi ở tàu Akagi và Kaga, việc này dự định sẽ tốn 1 tiếng rưỡi."
    "0745!"
    noti "Thông báo! Máy bay Tone 4, cái mà bị trễ lúc trước, đã phát hiện “10 tàu đối phương”."
    menu:
        "Dừng việc thay đổi vũ khí":                      ##############################
        "Chúng ta phải tấn công mọi tàu đối phương ở xung quanh vùng này để bảo vệ hạm đội trước khi quá muộn"
        "Rõ"
            jump a14
        "Tiếp tục thay đổi vũ khí để tấn công Midway":    ##############################
        "Midway vẫn là 1 mối đe dọa chúng ta cần phải phá hủy."
        "Rõ"
            jump a15

label a14: # Dừng việc thay đổi vũ khí
    scene plane14 with fade
    "1 điều tôi thấy lạ về thông báo này của Tone 4, \theo đường bay chỉ định, Tone 4 không thể đi qua hạm đội đối phương được\""
    "Nghĩa là Tone 4 đi sai đường, hoặc là vị trí của hạm đội bị thông báo sai."
    "Hơn nữa, “10 tàu đối phương” có thể có tàu sân bay, hoặc chỉ là tàu khu trực nhỏ."
    "Một tháng trước, tại trận đấu Biển San Hô, đô đốc Takagi đã\tấn công nhầm tàu khu trực của Mĩ thay vì tàu sân bay Mĩ. Chúng ta không thể làm lại lỗi lầm đó\""
    "Ngoài ra, tại sao lại có 1 hạm đội 240 dặm Bắc của Midway?\Không có lí do gì để có 1 hạm đội ở đây trừ khi đó là hạm đội tàu sân bay.\""
    "Quan trọng hơn, theo báo cáo, hạm đội đối phương đang đi vào vùng có gió.\Bình thường tàu sân bay cần có gió để phóng máy bay.\""
    menu:
        "Đó là tàu sân bay đối phương":
            jump a1819
        "Chỉ là tàu bình thường thôi":
            jump a1819
label a15: # Tiếp tục thay đổi vũ khí để tấn công Midway
    scene plane14 with fade
    "1 điều tôi thấy lạ về thông báo này của Tone 4, \theo đường bay chỉ định, Tone 4 không thể đi qua hạm đội đối phương được\""
    "Nghĩa là Tone 4 đi sai đường, hoặc là vị trí của hạm đội bị thông báo sai."
    "Hơn nữa, “10 tàu đối phương” có thể có tàu sân bay, hoặc chỉ là tàu khu trực nhỏ."
    "Một tháng trước, tại trận đấu Biển San Hô, đô đốc Takagi đã\tấn công nhầm tàu khu trực của Mĩ thay vì tàu sân bay Mĩ. Chúng ta không thể làm lại lỗi lầm đó\""
    "Ngoài ra, tại sao lại có 1 hạm đội 240 dặm Bắc của Midway?\Không có lí do gì để có 1 hạm đội ở đây trừ khi đó là hạm đội tàu sân bay.\""
    "Quan trọng hơn, theo báo cáo, hạm đội đối phương đang đi vào vùng có gió.\Bình thường tàu sân bay cần có gió để phóng máy bay.\""
    menu:
        "Đó là tàu sân bay đối phương":
            jump a161723
        "Chỉ là tàu bình thường thôi":
            jump a161723
label a1819: # Suy đoán tàu sân bay đối phương + Chỉ là tàu bình thường thôi
    scene phongdochoi with fade:
        size(1300,720)
    "Thông báo từ Tomonaga. Đội máy bay của Tomonaga dự định sẽ quay trở lại đây vào 0815."
    "Tin xấu là máy bay của họ sẽ hết nhiên liệu vào 0915. Các máy bay đó hạ cánh sẽ mất khoảng 30 phút."
    "Thế nên họ cần bắt đầu hạ cánh muộn nhất vào 0845 nếu chúng ta không muốn mất thêm máy bay."
    "Phóng máy bay tấn công sẽ tốn khoảng 45 phút thế nên chúng ta\có đến muộn nhất 0800 để phóng trước khi mất máy bay từ đội của Tomonaga.\""
    "Và tệ hơn nữa, tàu sân bay của chúng ta không\ thể đón và phóng máy bay cùng một lúc.\""
    menu:
        "Phóng máy bay tấn công ngay lập tức":                                ##############################################
        "Danh tính của đối phương vẫn chưa biết, còn vị trí thì còn khả nghi"
        "1 vài máy bay dự trữ vừa thay đổi vũ khí nên chỉ còn 64/78 máy bay tấn công được."
        "Nhưng trong chiến tranh tàu sân bay, ai tấn công trước người đấy thắng."
        "Rõ"
            jump a2122
        "Đợi thời gian nghĩ thêm":                                            ##############################################
        "Không máy bay nào của Tomonaga phải bị mất, có đủ thời gian để\chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy ba\""
        "Rõ"
            jump a2122
        "Phóng máy bay tấn công hạm đội đối phương sau khi Tomohaga hạ cánh": ##############################################
        "Chúng ta có 15 phút để suy nghĩ trước khi phải hy sinh máy bay từ đội của Tomonaga."
        "Rõ"
            jump a161723

label a2122: # phóng máy bay tấn công ngay + đợi thời gian nghĩ thêm
    "0753!"
    scene phongdochoi with fade:
        size(1300,720)
    show thuyenpho at right:
        size(450,720)
    menu:
        "Tất cả chuẩn bị súng phòng không":
            jump a26

label a161723: # suy đoán tàu sân bay đối phương + chỉ là tàu bình thường thôi + phóng máy bay sau khi tấn công hạm đội đối phương (sau khi Tomonaga hạ)
    "0753!"
    scene hiryuu1 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc! Máy bay địch xuất hiện ở phía đông nam"
    menu:
        "Tất cả chuẩn bị súng phòng không":
            jump a24
label a26: # 0753 tất cả chuẩn bị súng phòng không
    "0810!"
    scene hiryuu2 with fade
    "Tất cả máy bay địch đã nhắm vào con tàu Hiryuu của mình"
    "Có vẻ như chúng đang thả bom lươn, thay vì chĩa thẳng xuống."
    "Rõ ràng bọn Mĩ không có chút kinh nghiệm."
    menu:
        "Báo cáo tình hình":
            jump a27

label a24: # 0753 tất cả chuẩn bị súng phòng không
    "0810!"
    scene hiryuu2 with fade
    "Tất cả máy bay địch đã nhắm vào con tàu Hiryuu của mình"
    "Có vẻ như chúng đang thả bom lươn, thay vì chĩa thẳng xuống."
    "Rõ ràng bọn Mĩ không có chút kinh nghiệm."
    menu:
        "Báo cáo tình hình":
            jump a252829

label a27: # 0810 Báo cáo tình hình
    dmr "Hạm đội của chúng ta không có tổn thương gì.\1 máy bay zero đã bị mất, và đã bắn hạ được gần chục máy bay đối phương.\""
    menu:
        "Phóng máy bay tấn công ngay lập tức":                                  #####################################################
        tp "Thuyền trưởng, vì cuộc tấn công này, chúng ta đã không thể phóng máy bay tấn công đối phương"
        tp "Tại vì bây giờ đã quá 0800, tấn công đối phương bây giờ\sẽ khiến chúng ta phải hy sinh đa số máy bay trong đội của Tomonaga.\""
        tp "Thuyền trưởng có muốn đổi quyết định không?"
        "danh tính của đối phương vẫn chưa biết, vị trí đối phương thì còn khả nghi."
        "1 vài máy bay dự trũ vừa thay đổi vũ khí nên chỉ còn 64/78 máy bay tấn công được."
        "Nhưng trong chiến tranh tàu sân bay, ai tấn công trước người đấy thắng."
        "Nhưng đa số của 97 máy bay trong đội của Tomonaga sẽ bị mất."
            jump a252829
        "Phóng máy bay tấn công sau khi đội máy bay của Tomonaga hạ cánh":      #####################################################
        "Không máy bay nào của Tomonaga phải bị mất"
        "có đủ thời gian để chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy bay."
            jump a252829

label a252829: # phóng máy bay sau khi Tomohaga hạ cánh + phóng máy bay tấn công ngay lập tức + 0810 Báo cáo tình hình
    scene plane6 with fade
    noti "Phát hiện máy bay thả bom đối phương trên cao 200 dặm"
    "Với độ cao này, súng phòng không của chúng ta không có tác dụng gì cả."
    menu:
        "Chuẩn bị né":
            jump a30

label a30: # Chuẩn bị né
    "0820!"
    scene soryuu with fade
    "Bọn chúng đã tấn công Soryuu, Hiryuu và Akagi"
    "Nhưng ở trên độ cao đó, độ chính xác của đối phương cũng bị giảm"
    "Hạm đội của chúng ta không bị sát thương nào"
    noti "Thông báo! Thông tin đưa về từ máy bay trinh sát Tone 4"
    "Có lẽ chiếc tàu sân bay kia đi theo hạm đội chúng"
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":
        "Danh tính đối phương đã được xác nhận."
        "Với tàu sân bay, đối phương có thể tấn công bất cứ lúc nào."
        "Chúng ta phải tấn công trước! Nhưng lưu ý, tấn công lúc này sẽ chắc chắn mất hết 97 máy bay của đội Tomonaga."
        "Và chúng ta sẽ không có máy bay tiêm kích bảo kê máy bay thả bom vì chúng đã được sử dụng để bảo vệ hạm đội"
        "thế nên tỉ lệ chúng ta có thể tấn công đối phương an toàn là rất thấp."
        "Rõ"
            jump a3132
        "Phóng máy bay tấn công hạm đội đối phương sau khi đội máy bay của Tomonaga hạ cánh":
        "Không máy bay nào của Tomonaga phải bị mất"
        "có đủ thời gian để chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy bay."
        "Rõ"
            jump a3132

label a3132: # phóng máy bay sau khi Tomohaga hạ cánh + phóng máy bay tấn công đối phương ngay lập tức
    "0825!"
    scene ship12 with fade
    noti "Thông báo! Phát hiện ống nhòm của tàu ngầm đối phương!"
    "Tàu khu trục Arashi đã được cử để đi săn nó."
    scene black with fade
    "0827!"
    scene ship13 with fade
    noti "Phát hiện máy bay thả bom địch ở phía Đông Nam"
    menu:
        "Tất cả chuẩn bị súng phòng không":
            jump a33

label a33: # 0827 tất cả chuẩn bị súng phòng không
    "0839!"
    scene ship19 with fade
    menu:
        "Báo cáo tình hình":
        "Tất cả máy bay địch đã tấn công chiến hạm Haruna"
        "Bọn nó không thả bom trúng quả nào, và chúng ta đã bắn hạ được 2 máy bay địch"
        "Con tàu ngầm đối phương đã bắn trượt chiến hạm Kirishima của chúng ta,"
        "và hiện tại đang bỏ chạy, tàu khu trực Arashi của chúng ta vẫn đang đuổi theo."
            jump a34

label a34: # 0839 báo cáo tình hình
    scene plane11 with fade
    menu:
        "Cho Arashi tiếp tục đuổi theo":   ##########################################################
        "Con tàu ngầm đó vẫn là mối đe dọa lớn, một ngư lôi từ tàu ngầm đó có thể đánh chìm cả tàu sân bay."
        " Arashi sẽ trở lại sau khi tiêu diệt được tàu  ngầm hoặc là khi nó đi xa quá"
        "Rõ!"
            jump a35
        "Gọi Arashi quay lại tàu sân bay": ##########################################################
        "Không nên cho 1 con tàu tách riêng khỏi hạm đội, nó có thể bị tấn công riêng lẻ."
        "Rõ!"
            jump xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

label a35: # cho arashi tiếp tục đuổi theo
    scene ship2 with fade
    "Tinh thần của bọn Mĩ mãnh liệt hơn chúng ta đã tưởng, nhưng kĩ năng của họ thì thật đáng xấu hổ."
    "Với tình hình này, chúng ta chắc chắn sẽ giành được chiến thắng."
    "Máy bay đồng minh phát hiện! Đó là đội máy bay của đội Tomonaga đang trở lại."
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":                        ##########################################################################
        "Danh tính đối phương đã được xác nhận."
        "Với tàu sân bay, địch có thể tấn công bất cứ lúc nào."
        "Chúng ta phải tấn công trước!"
        "Nhưng lưu ý, tấn công lúc này sẽ chắc chắn mất hết 97 máy bay của đội Tomonaga."
        "Và chúng ta sẽ không có máy bay tiêm kích bảo vệ máy bay thả bom vì chúng đã được sử dụng để bảo vệ hạm đội"
        "thế nên tỉ lệ chúng ta có thể tấn công đối phương an toàn là rất thấp."
            jump a363839
        "Phóng máy bay tấn công hạm của địch sau khi đội máy bay của Tomonaga hạ cánh":   ##########################################################################
        "Đội máy bay của Tomonaga đã quay trở lại an toàn"
        "chúng ta không thể nhìn họ hy sinh máy bay được. "
        "Chúng ta còn thời gian để nạp nhiên liệu và đạn và tấn công sau khi đón họ trở về"
        "Rõ!"
            jump a37

label a37: # sau khi Tomohaga hạ cánh
    "0910!"
    scene ship8 with fade
    "Tất cả các phi công trong đội máy bay của Tomonaga đã hạ cánh an toàn."
    "Bây giờ chúng ta phải tính nước đi tiếp theo."
    menu:
        "Tấn công Midway":
        "Midway vẫn là mối đe dọa, chúng ta có thể tấn công hạm đội đối phương sau khi vô hiệu hóa Midway."
            jump a363839
        "Tấn công hạm đội đối phương":
        "Tàu sân bay của địch là đối tượng quan trọng nhất và đáng nguy hiểm nhất."
        "Mục đích chính của chiến dịch này là phá hủy tàu sân bay đối phương và bắt Mĩ phải đầu hàng."
        "Rõ!"
            jump a363839

label a363839: # tấn công hạm đội đối phương + tấn công midway + phóng máy bay tấn công hạm đội đối phương ngay lập tức
    "Chúng ta chỉ cần 45 phút là sẽ phóng được hàng loạt máy bay hùng mạnh"
    "0918"
    scene ship16 with fade
    noti "Thông báo, chúng ta đang bị tấn công bởi máy bay thả ngư lôi Mĩ từ phía Bắc."
    menu:
        "Dừng việc phóng máy bay và chuẩn bị súng phòng không":
            jump a40

label a40: # Dừng việc phóng máy bay và chuẩn bị súng phòng không
    scene ship4 with fade
    "Máy bay thả bom đối phương không hề có máy bay chiến đấu bảo vệ."
    "Bọn nó sẽ chỉ là mồi nhử cho các máy bay của chúng ta thôi."
    menu:
        "Báo cáo tình hình":
            jump a41

label a41: # Báo cáo tình hình
    "0937!"
    scene phongdochoi with fade:
        size(1300,720)
    dmr "Trong số 15 máy bay đối phương tấn công, chỉ có 3 cái đến gần được con tàu Soryuu của chúng ta, và chỉ có 1 máy bay địch bắn được ngư lôi, nhưng mà trượt"
    menu:
        "Tiếp tục phóng máy bay tấn công":
            jump a42

label a42: # tiếp tục phóng máy bay tấn công
    "0940!"
    scene phongdochoi with fade:
        size(1300,720)
    noti "Thông báo, chúng ta đang bị tấn công bởi máy bay thả ngư lôi Mĩ từ phía Nam."
    "Chết tiệt! Chúng ta chỉ cần 45 phút không bị gián đoạn để tấn công."
    "Nhưng lúc đang bị tấn công thì không thể phóng máy bay được."
    "Và các máy bay địch này chỉ có thể là từ tàu sân bay đối phương, nhưng theo thông báo, hạm đội đối phương vẫn ở ngoài tầm tấn công."
    menu:
        "Dừng phóng máy bay và chuẩn bị súng phòng không":
            jump a43

label a43: # dừng việc phóng máy bay và chuẩn bị tấn công
    "0985!"
    scene phongdochoi with fade
        size(1300,720)
    menu:
        "Báo cáo tình hình.":
            jump a44

label a44: # Báo cáo tình hình
    scene phongdochoi with fade
        size(1300,720)
    show thuyenpho at right:
        size(450,720)
    tp "Bọn chúng đã tấn công con tàu Kaga của chúng ta, nhưng không phát nào trúng, chúng ta chỉ bị mất 1 từ máy bay Zero"
    menu:
        "Tiếp tục phóng máy bay tấn công":
        "Rõ!"
            jump a35

label a45: # tiếp tục phóng máy bay tấn công
    "1010"
    scene ship19 with fade
    noti "Phát hiện máy bay thả ngư lôi địch từ phía đông nam!"
    "Đây quả là một trò đùa, hơn 50 phút rồi có 3 đợt tấn công liên tiếp, trì hoãn đợt tấn công của chúng ta."
    "Điều này chứng tỏ đối phương phải có hơn 1 tàu sân bay."
    "Nhưng từ nãy đến giờ chỉ có máy bay thả ngư lôi, vậy máy bay thả bom của Mĩ đâu?"
    scene black with fade
    "1020"
    scene ship19 with fade
    "Tin xấu! Đợt tấn công lần này của kẻ địch có máy bay chiến đấu."
    "Quân địch đang dùng chiến thuật di chuyển mới, và rất nhiều máy bay zero của chúng ta đang bị bắn hạ"
    "Điều này khiến cho tất cả máy bay zero đều đã ra ngăn cản máy bay địch, khiến hạm đội chúng ta không hề có máy bay bảo vệ trên đầu"
    menu:
        "Gọi máy bay chiến đấu bảo vệ trên đầu":               #######################################################
        "Chúng ta cần có máy bay bảo vệ hạm đội trên\đầu đề phòng trường hợp mình bị tấn công từ hướng khác\""
            jump a4647
        "Để tất cả máy bay tập trung tấn công máy bay địch":   ########################################################
        "Chúng ta cần tiêu diệt đối thủ trước khi chúng nó có thể lại gần, cách này sẽ hiệu quả hơn."
            jump a4647

label a4647: # gọi máy bay quay lại bảo vệ + để tất cả máy bay tập trung tấn công máy bay địch
    scene atakagi1 with fade
    noti " Thông báo! Gần 50 máy bay thả bom Mĩ đang tiến tới từ cả phía Bắc và phía Nam,\chúng nó đã tiến tới quá gần mà không bị phát hiện và đang bắt đầu tấn công hạm đội của ta\""
    "Chúng ta không hề có máy bay nào sẵn sàng bảo vệ cả"
    "Liệu đây là cái kết..."
    scene black with fade
    "1022-1026"
    scene ship15 with fade
    tp "Đô đốc, nhìn kìa, Kaga vừa bị trúng 4 quả bom"
    "Cô ấy đang cháy"
    scene atakagi2 with fade
    tp "Đô đốc! Bên kia, Soryuu cũng đang bị tấn công"
    "Boom!"
    "Cô ấy cũng đang bị nổ từ bên trong! Lửa ở khắp nơi."
    "Chỉ còn chúng ta và Hiryuu thôi"
    noti "Thông báo, 3 máy bay thả bom đối phương đã thay đổi hướng, chúng đang ngắm về hướng chúng ta"
    scene atakagi3 with fade
    "Boom! (1 quả bom đã rơi trượt tàu Akagi)"
    scene deakagi2 with fade
    "Boom! ( quả bom thứ 2 đã rơi trượt tàu Akagi)"
    scene plane14 with fade
    "Còn máy bay cuối cùng đang nhắm thẳng tới sàn bay của chúng ta!"
    "BOOM!"
    scene black with fade
    "1026"
    menu:
        "báo cáo tình hình"
            jump a49

label a49: # Báo cáo tình hình
    scene plane15 with fade
    show thuyenpho at right:
        size(480,720)
    tp "Tất cả tàu sân bay của chúng ta đều có vũ khí, máy bay và nhiên liệu ở dưới sàn bay."
    tp "Và chỉ với 1 quả bom, nó đã khiến cả con tàu Akagi bị cháy"
    tp "Số phận của Kaga, Soryuu đều cũng thế."
    tp "Chúng ta chỉ còn Hiryuu đã né được ngư lôi từ máy bay địch và còn hoạt động được"
    tp "Đô đốc, con tàu Akagi không thể bị cứu được nữa.\Thuyền trưởng hãy chuyển sang con tàu tuần dương nagara để tiếp tục chỉ huy trận chiến\""
    menu:
        "Chìm cùng với tàu":          #############################################
        "Thuyền trưởng có trách nghiệm bảo vệ con tàu và thủy thủ của mình, khi tàu chìm,\thuyển trưởng có truyền thống ở lại trên con tàu đang chìm để bảo vệ danh vọng của mình\""
            jump a51
        "Chỉ huy tiếp từ tàu Nagara":     ##############################################
        "Mình là chỉ huy của cả hạm đội, không có mình là Nhật Bản sẽ\thua trận chiến này, chúng ta cần phải trả thù để bảo toàn được danh vọ\""
            jump a50

label a51:  #ending die 2
    menu:
        "Ending 2 (die)"
            jump ending2
label a50: # tháo chạy bằng xuồng và chỉ huy tiếp từ tàu Nagara
    scene ship5 with fade
    show thuyenpho at right:
        size(480,720)
    tp "Chào mừng thuyền trưởng trên con tàu tuần dương hạng nhẹ Nagara, kỳ hạm tạm thời của chúng ta."
    tp "Chúng ta còn mỗi con tàu sân bay Hiryuu được chỉ huy bởi Yamaguchi."
    tp "Hiryuu vẫn có đội máy bay thả bom giỏi nhất của Nhật Bản,\ những phi công trẻ của chúng ta đã sẵn sàng để trả thù, vì danh vọng của tổ quốc.\""
    tp "Nhưng theo số máy bay đối phương,\ tôi dự đoán là Mĩ đang có 3 tàu sân bay đang tham gia trận chiến này\""
    tp "Chúng ta có lệnh từ đô đốc Yamamoto, chỉ huy toàn bộ hải quân Nhật Bản."
    tp "Ông ấy muốn chúng ta tìm và tấn công hạm đội Mỹ trực tiếp\ Ông ấy đã ra lệnh cho một số chiến hạm làm viện trợ cho chúng ta.\""
    tp "Hơn nữa, 2 tàu sân bay hạng nhẹ Junyo và Ryujo cũng sẽ đến tiếp viện cho chúng ta."
    tp "Nhưng tất cả viện trợ này đang ở rất xa chúng ta và sẽ không có thể đến kịp thời gian được"
    tp "Tại vì hạm đội đối phương có vẻ như đang đi theo hướng Đông Nam,\ và đang tăng khoảng cách với mình. Thế nên chỉ có Hiryuu là có thể tấn công thôi\""
    tp "Cả tương lai của Nhật Bản đang đặt trên vai của thuyền trưởng."
    menu:
        "Rút lui":
        "Tình hình đang là 3 vs 1, Hiyruu là tàu sân bay duy \nhất của Kido Butai, và chúng ta phải bảo vệ cô ấy với mọi giá.\""
            jump a52
        "Đuổi theo":
        "Lựa chọn duy nhất mà mọi người Nhật Bản có thể chọn, chúng ta vẫn còn có cơ hội"
        "để lật đảo cuộc chiến này. Kẻ địch đã chạy ra ngoài tâm của chúng ta,"
        "nhưng chúng ta có thể đuổi kịp trong khoảng thời gian ngắn."
            jump a51


label a52:
    menu:
        "Ending 1 (fire)"
            jump ending1

label a51:
    scene phongdochoi with fade
        size(1300,720)
    show thuyenpho at right:
        size(480,720)
    tp "Tuyệt vời! Để tôi bảo các phi công của chúng ta chuẩn bị."
    showw black with fade
    "1054!"
    "Chúng ta đã đuổi kịp hạm đội đối phương"
    menu:
        "Phóng máy bay phản công":
            jump a53

label a52:
    scene phongdochoi with fade
        size(1300,720)
    menu:
        "Rúi lui":
            jump a55
        "Tiếp tục tấn công":
            jump a54
label a55:
    menu:
        "Ending 1 (fire)":
            jump ending1

label a54:
    scene ship7 with fade
    menu:
        "Đi hướng Tây Bắc":
            jump a56
        "Đi hướng Đông Nam":
            jump a57

label a56:
    menu:
        "Ending 4 (live & job)":
            jump ending4

label a57:
    scene ship5 with fade
    menu:
        "Rẽ trái khẩn cấp":
            jump a5859
        "Đi thẳng tiếp":
            jump a5859

label a5859:
    menu:
        "Báo cáo tình hình":
            jump a60

label a60:
    scene phongdochoi with fade 
        size(1300,720)
    show thuyenpho at right:
        size(480,720)
    tp "Thông báo từ đội máy bay vừa quay trở lại"
    "Chỉ có 5/13 máy bay thả bom Val trở lại, 1/4 máy bay zero trở lại. "
    "Nếu tiếp tục như thế này, chúng ta có thể sẽ hết sạch máy bay cho đến tối mất."
    tp "Đổi lại, chúng ta chỉ bắt hạ được 1 máy bay Wildcat từ Mĩ."
    "Tin tốt từ những phi công quay trở lại."
    "Họ đã để 1 tàu sân bay Mĩ, cháy ở giữa biển."
    menu:
        "Rút lui":
            jump a61

label a61:
    menu:
        "Ending 4 (historical, live & job)":
            jump ending4



    

########################################################################################################################
#ALL ENDING IS HERE

label ending1:
    
label ending2:

label ending3:

label ending4:
