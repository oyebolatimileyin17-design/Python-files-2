import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

hours_studied = np.array([[1], [2], [3], [4], [5]])
exam_scores = np.array([50, 55, 65, 70, 80])

model = LinearRegression()
model.fit(hours_studied, exam_scores)

# Generate points along the line for plotting (1 to 6 hours)
line_x = np.array([[i] for i in range(1, 7)])
line_y = model.predict(line_x)

plt.scatter(hours_studied, exam_scores, color='blue', label='Actual scores')
plt.plot(line_x, line_y, color='red', label="Model's learned line")
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.title('Hours Studied vs Exam Score')
plt.legend()
plt.show()