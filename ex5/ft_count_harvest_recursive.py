
def ft_count_harvest_recursive(days=-1, count=1):
    if days == -1:
        days = int(input("Days until harvest: ")) + 1
    if count < days:
        print(f"Day {count}")
        ft_count_harvest_recursive(days, count + 1)
    if count == days:
        print("Harvest time!")


ft_count_harvest_recursive()
