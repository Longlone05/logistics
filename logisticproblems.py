from math import ceil
packages = 500*2000 # tổng số gói hàng
truck = 100 # số gói hàng trên 1 chuyến
arena1 = packages // 2 # tổng gói hàng khu vự 1
arena2 = packages // 4 # tông gói hàng khu vực 2
arena3 = packages // 4 # tổng gói hàng khu vực 3
truck1 = 0.5 # thời gian di chuyển khu vực 1
truck2 = 1 # thời gian di chuyển khu vực 2
truck3 = 2 # thời gian di chuyển khu vực 3
tg_tuan = 7*24 ## thời gian trong 1 tuần
xe_gh = 100 #giới hạn xe ở câu 2

def cau_1():
    xe = ceil(arena1 / (truck * (tg_tuan / truck1)))
    xe += ceil(arena2 / (truck * (tg_tuan / truck2)))
    xe += ceil(arena3 / (truck * (tg_tuan / truck3)))
    print('So xe toi thieu de cho het hang trong 1 tuan la:', xe, 'xe')

def cau_2():
    tg = arena1 / (xe_gh * truck) * truck1
    tg += arena2 / (xe_gh * truck) * truck2
    tg += arena3 / (xe_gh * truck) * truck3
    ngay = int(tg // 24); tg -= ngay*24
    gio = int(tg); tg -= gio; tg *= 60
    phut = int(tg); tg -= phut; tg *= 60
    giay = int(tg)
    print(f'thời gian tối thiểu để 100 xe chở hết hàng là {ngay} ngày {gio} giờ {phut} phút {giay} giây')
def main():
    cau_2()

# begin
main()
