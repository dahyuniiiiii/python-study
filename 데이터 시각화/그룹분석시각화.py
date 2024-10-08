import seaborn as sns
import matplotlib.pylab as plt
iris = sns.load_dataset("iris") 
df2 = iris.groupby(iris.species).mean() #종별로 각 특성의 평균 계산
#groupby: 데이터를 특정 기준으로 묶음, mean() 함수: 그룹화된 데이터의 평균을 구함
df2.columns.name = "feature" #열 이름
print(df2) #평균값
#<Feature별 평균>
df2.plot.bar(rot=0) #막대그래프
#rot=0: x축 레이블의 회전 각도를 0도로 설정하여, 레이블을 수평으로 표시
plt.title("각 종의 Feature별 평균")
plt.xlabel("평균")
plt.ylabel("종")
plt.ylim(0, 8) #y축 범위
plt.show()
#Feature의 종별 평균>
# df2.T.plot.bar(rot=0)
# plt.title("각 Feature의 종 별 평균")
# plt.xlabel("Feature")
# plt.ylabel("평균")
# plt.show()