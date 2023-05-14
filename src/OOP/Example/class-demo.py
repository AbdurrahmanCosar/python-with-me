# Comment isminde bir sınıf oluşturunuz
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun
# 3 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız


class Comment:
    def __init__(self, username, text, likes = 0, dislikes = 0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes


c1 = Comment("Abduley", "Çok iyi bir repo", 5, 2)
c2 = Comment("pastel", "Gayet Güzel")
c3 = Comment("minidev", "Çok kötü", 49, 53)

comments = [c1, c2, c3]

for comment in comments:
    print(f"{comment.username}: {comment.text}")
    print(f"likes: {comment.likes} - dislikes: {comment.dislikes}\n")