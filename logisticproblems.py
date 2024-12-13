import math

# Dữ liệu
tong_so_hang = 2000 * 500  # Tổng số gói hàng
so_hang_moi_xe = 100       # Số gói hàng mỗi xe tải chở được
tong_thoi_gian = 7 * 24 * 60  # Tổng số phút trong 1 tuần
thoi_gian = {
    "Khu vực 1": 30,  # 30 phút/chuyến
    "Khu vực 2": 60,  # 60 phút/chuyến
    "Khu vực 3": 120  # 120 phút/chuyến
}
so_xe = 100  # Số xe tải giả định
def tinh_so_chuyen_can_thiet(tong_so_hang, so_hang_moi_xe):
    return {
        "Khu vực 1": math.ceil((tong_so_hang * 0.5) / so_hang_moi_xe),
        "Khu vực 2": math.ceil((tong_so_hang * 0.25) / so_hang_moi_xe),
        "Khu vực 3": math.ceil((tong_so_hang * 0.25) / so_hang_moi_xe)
    }

def tinh_xe_toi_thieu(so_chuyen, thoi_gian, tong_thoi_gian):
    return sum(math.ceil(so_chuyen[khu_vuc] / (tong_thoi_gian // thoi_gian[khu_vuc])) for khu_vuc in so_chuyen)

def tinh_thoi_gian_toi_thieu(tong_so_chuyen, thoi_gian, so_xe):
    so_chuyen_moi_phut = sum(so_xe / thoi_gian[khu_vuc] for khu_vuc in thoi_gian)
    thoi_gian_phut = math.ceil(tong_so_chuyen / so_chuyen_moi_phut)
    return thoi_gian_phut, thoi_gian_phut / (24 * 60)



# Tính toán
so_chuyen = tinh_so_chuyen_can_thiet(tong_so_hang, so_hang_moi_xe)
tong_so_xe = tinh_xe_toi_thieu(so_chuyen, thoi_gian, tong_thoi_gian)
tong_so_chuyen = sum(so_chuyen.values())
thoi_gian_phut, thoi_gian_ngay = tinh_thoi_gian_toi_thieu(tong_so_chuyen, thoi_gian, so_xe)

# In kết quả
print(f"Cần tối thiểu {tong_so_xe} xe tải để vận chuyển hết hàng hóa trong 1 tuần.")
print(f"Với 100 xe tải, thời gian tối thiểu để vận chuyển hết hàng hóa là {thoi_gian_phut} phút (~{thoi_gian_ngay:.2f} ngày).")
