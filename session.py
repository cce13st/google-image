from pykakao import kakaotalk

kakao = kakaotalk()
if kakao.auth("ccelest@kaist.ac.kr", "kt2714", "MBPR", "1"):
    print kakao.session_key
    print kakao.user_id
else:
    print "auth failed"
