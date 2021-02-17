def arrayOfProducts(array):
    bucket_list = [0] * len(array)
    for idx in range(0, len(bucket_list)):
        product_value = 1
        for idx_ in range(0, len(bucket_list)):
            if idx != idx_:
                product_value *= array[idx_]
        bucket_list[idx] = product_value
    return bucket_list


if __name__ == '__main__':
    l = [5, 1, 4, 2]
    print(arrayOfProducts(l))
