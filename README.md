## The sum of the shortest distance between two points

The sum of the shortest distance between two points from the total of three types of input numbers

Three old friends want to meet each other on the occasion of the Persian New Year. Azarmehr, Azargoun, and Mehrayan plan to meet at a point where their houses lie on a straight line (the x-axis). Azarmehr's house is located at point x1, Azargoun's house is at point x2, and Mehrayan's house is at point x3. They want to travel the minimum total distance to meet each other at a single point. Given x1, x2, and x3, calculate the minimum distance that these three friends must travel in total to meet each other at a single point. Please print the answer without a decimal point if it is an integer. Note that we are interested in the minimum distance they have to travel, not the meeting location itself.

## Input:
6 9 10

## Output:
4

------------------------------------------------------------------------------
## مجموع کمترین مسافت بین دو نقطه از مجموع سه نوع عدد ورودی 

به مناسبت عید نوروز سه دوست قدیمی می خواهند همدیگر را ملاقات کنند. آذرمهر، آذرگون و مهرآئین قصد دارند در یک نقطه همدیگر را ملاقات کنند. منزل این سه نفر روی خط راست قرار دارد (محور xها) خانه ی آذرمهر در نقطه ی x1 قرار دارد، خانه ی آذرگون در نقطه ی x2 قرار دارد و خانه ی مهرآئین در نقطه ی x3 قرار دارد. آنها در مجموع می خواهند کمترین مسافت را طی کنند. با در دست داشتن x1 x2 x3 کمترین مسافتی که این سه در مجموع باید طی کنند تا در یک نقطه همدیگر را ملاقات کنند را محاسبه کنید. لطفا در صورتی که جواب عدد صحیح شد آن را بدون نقطه ی عدد اعشاری چاپ کنید مثلا در نمونه ی زیر اگر چاپ کنید 6.0 غلط است.

## ورودی نمونه
```python
6 9 10
```
## خروجی نمونه
```python
4
```
کد برنامه 
```python
list1 = input().split()

list2 = [int(item) for item in list1]

list3 = sorted(list2)

results=list3[-1]-list3[0]

print(results)
```
