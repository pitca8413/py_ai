import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

# 화면에 텍스트 이미지 출력
print(digits.images[21])

# matplot을 사용해 이미지 출력
plt.imshow(digits.images[21], cmap='Greys')
plt.show()