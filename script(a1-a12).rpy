define tp = Character("Thuyền Phó", color="c8ffc8")
#The game start here

label start:#(0430) thuyền trưởng phóng máy bay về phía trước
    scene black with fade
    "0430!"
    scene phongdochoi with fade
    show thuyenpho at right:
        size(450,720)
    tp "Thuyền trưởng, theo như kế hoạch, bây giờ chúng ta phải phóng\"các máy bay trinh thám để quan sát mặt trận phía trước\""
    menu:
        "Ra lệnh cho máy bay trinh thám":
            jump a3
        "Chúng ta không cần máy bay trinh thám":
            jump a2
    
label a3: #Ra lệnh cho máy bay trinh thám
    scene plane2 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Thuyền trưởng, hãy cho máy bay tấn công hải quân Hoa Kì ở Midway nhưu theo kế hoạch"
    menu:
        "không phải bây giờ":  #
            "Đây là thời điểm tấn công theo kế hoạch, thời tiết thuận lợi\"và máy bay đủ tầm, các phi công đều đã chuẩn bị\""
            jump a4 
        "Tân công Midway":     #
            "Nếu chúng ta trì hoãn sự tấn công, thì đối phương sẽ có thêm thời gian\chuẩn bị hoặc còn có thể phản công, thời tiết có thể trở nên xấu đi\""
            jump a5
label a2: # Chúng ta không cần máy bay trinh thám (random)
    scene black with fade
    "Bạn đã chết"
    return
label a4: # không phải bây giờ (random) 
    scene black with fade
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
    tp "Thuyền trưởng! Một máy bay Mĩ Catalina PBY đã phát hiện\ra hạm đội của chúng ta. Chúng ta đã mất yếu tố bất ngờ\""
    tp "Tệ hơn nữa, máy bay thả bom của chúng ta chưa đến đảo Midway,\có nghĩa là máy bay Mĩ ở đảo Midway có thể tấn công hạm đội của t bất cứ lúc nào.\""
    tp "Chúng ta phải làm sao đây"
    menu: 
        "Không cho thêm máy bay bảo vệ":    #
        "Chúng ta đã có nhiều máy bay đang bay trên đầu để bảo vệ hạm đội.\Hơn nữa, đối phương không thể phản ứng nhanh đến thế được, chúng ta sẽ có thừa thời gian để chuẩn bị một khi phát hiện máy bay địch\"" 
            jump a6
        "Cho thêm máy bay bảo vệ":          #
        "Có càng nhiều máy bay bảo vệ hạm đội càng an toàn,\ nhưng phải dùng các máy bay dự trữ, chúng ta sẽ không sẵn sàng nếu phát hiện hạm đội đối phương\""
            jump a7
label a6: # "0532" cho máy bay bảo vệ trước khi bị tấn công
    scene black with fade
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
    tp "Thuyền trưởng! Phi công Tomonaga sau khi tấn công Midway báo rằng\chúng ta cần 1 đợt tấn công nữa mới vô hiệu hóa được hòn đảo.\""
    tp "Hơn nữa, máy bay địch đang tiến tới hạm đội"
    menu:
        "Phóng máy bay bảo vệ":                            #
        "Đây là một hành động rất nguy hiểm, khi đang bị tấn công, tàu sân bay không thể phóng thêm máy bay mới"
        "Rõ, tôi chúc thuyền trưởng may mắn cho cuộc tấn công sắp tới"
            jump a9
        "Không phóng thêm máy bay, tập trung né":          #
        "Khi đang bị tấn công, các tàu sân bay tuyệt đối không được phóng máy bay mới, vì điều này sẽ làm giảm sự cơ động của tàu sân bay, và khiến tàu sân bay dễ bị cháy nổ hơn"
            jump a8
label a7: # "0532" ko cho thêm máy bay bảo vệ trước khi bị tấn công
    scene black with fade
    "0700!"
    scene ship10 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Thuyền trưởng! Phi công Tomonaga sau khi tấn công Midway báo rằng\chúng ta cần 1 đợt tấn công nữa mới vô hiệu hóa được hòn đảo.\""
    tp "Hơn nữa, máy bay địch đang tiến tới hạm đội"
    menu:
        "Phóng máy bay bảo vệ":                            #
        "Đây là một hành động rất nguy hiểm, khi đang bị tấn công, tàu sân bay không thể phóng thêm máy bay mới"
        "Rõ, tôi chúc thuyền trưởng may mắn cho cuộc tấn công sắp tới"
            jump a9
        "Không phóng thêm máy bay, tập trung né":          #
        "Khi đang bị tấn công, các tàu sân bay tuyệt đối không được phóng máy bay mới, vì điều này sẽ làm giảm sự cơ động của tàu sân bay, và khiến tàu sân bay dễ bị cháy nổ hơn"
            jump a8
            
label a9: # "0700" phóng máy bay bảo vệ
    scene black with fade
    menu:
        "Ending 4 (die)":
            jump ending4
label a8: # "0700" né máy bay địch, không phóng máy bay ta (lần 1)
    scene black with fade
    "0700!"
    scene deakagi1 with fade
    menu:
        "Né máy bay địch không phóng máy bay ta":
        jump a10
label a10: # "Some time later" sử dụng súng phòng không lần 1
    scene black with fade
    "Some time later"
    scene deakagi2 with fade
        show thuyenpho at right:
            size(450,720)
        tp "Cẩn thận thuyền trưởng! 4 máy bay thả ngư lôi đang ở bên phía cảng"
        menu: 
            "Sử dụng súng phòng không":
                jump a11
label a11: # Sử dụng súng phòng không lần 2
    scene atakagi1 with fade
    menu: 
        "Sử dụng súng phòng không lần 2":
            jump a12
label a12: # Báo cáo tình hình chiến dịch đợt 1
    scene phongdochoi with fade
    show thuyenpho at right:
        size(450,720)
    "Damage report" "Chúng ta đã mất 2 máy bay Zero"
    "Damage report" "Các con tàu còn lại"
    "Damage report" "Trên bầu trời đã hết máy bay địch, cuộc tấn công của địch đã kết thúc."
    "Damage report" "Và đến bây giờ vẫn chưa có thông báo gì từ máy bay trinh thám."
    scene black with fade
    "0715!"
    scene phongdochoi with fade
        size(450,720)
    tp "Thuyền trưởng, tiện thể đang trong thời gian an toàn, ngài cần trả lời yêu cầu của Tomonaga\Chúng ta cần 1 đợt nữa mới phá hủy được sân bay ở Midway.\""
    menu:
        "Tấn công bằng đội máy bay của Tomonaga":
        "Đợi đội máy bay của Tomonaga quay trở lại, tiếp nhiên liệu và vũ khí, rồi quay lại tấn công"
        "Lựa chọn này sẽ tốn rất nhiều thời gian, quân Mĩ có thể sửa lại sân bay và chuẩn bị phòng thủ, sẽ dẫn đến thêm mạng chết"
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
    scene atakagi2 with fade
    scene atakagi3 with fade


    
