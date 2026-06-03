import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# 한글 폰트 설정
# ============================
if sys.platform == "win32":
    plt.rc("font", family="Malgun Gothic")
elif sys.platform == "darwin":
    plt.rc("font", family="AppleGothic")

plt.rc("axes", unicode_minus=False)

# ============================
# 데이터 불러오기
# ============================
print("<역대 흥행 영화 데이터 분석>")
print("-" * 50)

try:
    movie = pd.read_csv(
        "역대박스오피스.csv",
        skiprows=4,
        encoding="utf-8"
    )
except Exception as e:
    print(f"파일을 불러오는 중 오류가 발생했습니다: {e}")
    sys.exit()

# ============================
# 데이터 확인
# ============================
print("\n[1] 상위 5개 데이터")
print(movie.head())

print("\n[2] 데이터 정보")
print(movie.info())

# ============================
# 결측치 및 중복 확인
# ============================
print("\n[3] 결측치 확인")
print(movie.isna().sum())

print("\n[4] 중복 데이터 개수")
print(movie.duplicated().sum())

# ============================
# 숫자형 변환
# ============================
numeric_cols = [
    "매출액",
    "관객수",
    "스크린수",
    "상영횟수"
]

for col in numeric_cols:
    movie[col] = (
        movie[col]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

# ============================
# 기본 통계
# ============================
print("\n[5] 기본 통계")

print(f"총 영화 수 : {len(movie)}편")

print(f"평균 관객수 : {movie['관객수'].mean():,.0f}명")
print(f"최대 관객수 : {movie['관객수'].max():,.0f}명")

print(f"평균 스크린수 : {movie['스크린수'].mean():.1f}개")
print(f"최대 스크린수 : {movie['스크린수'].max():.0f}개")

print(f"평균 상영횟수 : {movie['상영횟수'].mean():,.0f}회")
print(f"최대 상영횟수 : {movie['상영횟수'].max():,.0f}회")

# ============================
# 대표국적 분석
# ============================
print("\n[6] 대표국적별 영화 수")

country_count = movie["대표국적"].value_counts()

print(country_count)

plt.figure(figsize=(8, 8))

plt.pie(
    country_count,
    labels=country_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("대표국적별 영화 비율")

plt.show()

# ============================
# 관객수 분포 분석
# ============================
plt.figure(figsize=(10, 6))

sns.histplot(
    movie["관객수"],
    bins=20,
    kde=True
)

plt.title("관객수 분포")
plt.xlabel("관객수")
plt.ylabel("영화 수")

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()

# ============================
# 관객수 TOP 10 영화
# ============================
print("\n[7] 관객수 TOP 10 영화")

top10 = movie.sort_values(
    by="관객수",
    ascending=False
).head(10)

print(
    top10[
        ["영화명", "관객수"]
    ]
)

plt.figure(figsize=(12, 6))

sns.barplot(
    data=top10,
    x="영화명",
    y="관객수"
)

plt.title("관객수 TOP 10 영화")
plt.xlabel("영화명")
plt.ylabel("관객수")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.show()

print("\n프로그램이 정상적으로 종료되었습니다.")