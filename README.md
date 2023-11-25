# University System of Taiwan Graduate_time parser

> forked from [DeNT15T/Graduate_time_parser](https://github.com/DeNT15T/Graduate_time_parser)

## 簡介

根據教授名稱，去論文系統爬取其學生畢業時長的小工具

## 用法

去下面的網址按 run ，我只有對交大特別修，跑起來應該沒問題，如果有他校需求或有 bug 的話可以發 issue 告知我

https://replit.com/@lkvlkvlkv/Graduatetimeparser

## 更新紀錄

2023-11-25 : 修了一些 bug ( 自己看 commit )

2023-11-22 : 更新交大學號轉換規則

----下面是原作者的更新紀錄----

2020-11-13 : fix some link bug

2018-8-23 update: 支援顯示口試日期

2018-8-18 update: 支援系所過濾

2018-8-17 update: 支援中央、清大、陽明

計算方式：x = 畢業年 - 入學年

x == 1 : 兩年準時畢業 </br>
x == 2 : 兩到三年畢業 </br>
x == 3 : 三到四年畢業 </br>
x >= 4 : 四年以上畢業 </br>

僅供參考
