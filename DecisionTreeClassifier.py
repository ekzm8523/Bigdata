import pandas as pd

df = pd.read_csv('data/titanic.csv')
# 상위 5개의 정보만 출력
# print(df.head())

# data Frame 의 정보를 출력
# print(df.info())

# 숫자형 변수에 대한 5-Number summary 요약 수치(통계량)
# print(df.describe())

# 생존여부별 데이터 건수 카운트
# print(df['Survived'].value_counts())


# 생존여부 차트 시각화
import seaborn as sns # Matplotlib를 기반으로 다양한 색상 테마와 통계용 차트 등의 기능을 추가한 시각화 패키지
import matplotlib.pyplot as plt # 본격적 시각화 라이브러

# sns.countplot(x="Survived", data=df)
# plt.title("Survived")
# plt.show()

# sns.countplot(x="Sex", data=df)
# plt.title("Passengers by class")
# plt.show()
# print(df.pivot_table(index="Survived", columns="Sex", aggfunc="size"))
# pd.crosstab(df['Sex'], df['Survived'], margins=True).style.background_gradient(cmap='summer_r')

# 성별에 따른 생존여부 차트
# -> 여성이 남성보다 생존할 가능성이 더 높게 분포함
# sex_df = df.groupby(['Sex', 'Survived'])['Survived'].count().unstack('Survived')
# sex_df.plot(kind='bar', figsize=(20,10))
# plt.title('Sex')
# plt.show()

y_position = 1.02
f, ax = plt.subplots(1, 2, figsize=(18, 8))
# 등급별 데이터 건수 카운트, 3등급 > 1등급 > 2등급
df['Pclass'].value_counts().plot.bar(color=['#CD7F32','#FFDF00','#D3D3D3'], ax=ax[0])
ax[0].set_title('Number of Passengers By Pclass', y=y_position)
ax[0].set_ylabel('Count')
# 등급별 생존여부 건수 카운트
# -> 1등급 탑승자의 생존율이 가장 높고 3등급 탐승자의 생존율이 가장 낮다.
sns.countplot('Pclass', hue='Survived', data=df, ax=ax[1])
ax[1].set_title('Pclass: Survived vs Dead', y=y_position)
plt.show()

