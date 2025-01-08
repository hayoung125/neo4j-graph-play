CREATE (파이썬 프로그래밍 기초:lecture {name: '파이썬 프로그래밍 기초', instructor: '김호열', learning_time: '10시간', launch_date: '2020-01-01', rating: 4.5})
CREATE (자바스크립트 완벽 가이드:lecture {name: '자바스크립트 완벽 가이드', instructor: '이수진', learning_time: '12시간', launch_date: '2020-02-15', rating: 4.7})
CREATE (웹 개발의 모든 것:lecture {name: '웹 개발의 모든 것', instructor: '박민수', learning_time: '15시간', launch_date: '2020-03-10', rating: 4.6})
CREATE (데이터베이스 기초:lecture {name: '데이터베이스 기초', instructor: '최지훈', learning_time: '8시간', launch_date: '2020-04-20', rating: 4.4})
CREATE (머신러닝 입문:lecture {name: '머신러닝 입문', instructor: '김영희', learning_time: '20시간', launch_date: '2020-05-30', rating: 4.8})
CREATE (안드로이드 앱 개발:lecture {name: '안드로이드 앱 개발', instructor: '이상훈', learning_time: '25시간', launch_date: '2020-06-15', rating: 4.5})
CREATE (클라우드 컴퓨팅 기초:lecture {name: '클라우드 컴퓨팅 기초', instructor: '정수민', learning_time: '18시간', launch_date: '2020-07-01', rating: 4.3})
CREATE (UI/UX 디자인 기초:lecture {name: 'UI/UX 디자인 기초', instructor: '김지현', learning_time: '14시간', launch_date: '2020-08-10', rating: 4.6})
CREATE (사물인터넷(IoT) 기초:lecture {name: '사물인터넷(IoT) 기초', instructor: '이재훈', learning_time: '22시간', launch_date: '2020-09-05', rating: 4.7})
CREATE (사이버 보안 기초:lecture {name: '사이버 보안 기초', instructor: '최민수', learning_time: '16시간', launch_date: '2020-10-20', rating: 4.5})


CREATE (김호열:instructor {name: '김호열', college: '서울대학교', career: '10년', position: '교수', organization: '서울대학교 컴퓨터공학부'})
CREATE (이수진:instructor {name: '이수진', college: '고려대학교', career: '8년', position: '강사', organization: '고려대학교 정보대학'})
CREATE (박민수:instructor {name: '박민수', college: '연세대학교', career: '12년', position: '부교수', organization: '연세대학교 소프트웨어학과'})
CREATE (최지훈:instructor {name: '최지훈', college: 'KAIST', career: '5년', position: '조교수', organization: 'KAIST 전산학부'})
CREATE (김영희:instructor {name: '김영희', college: 'POSTECH', career: '7년', position: '강사', organization: 'POSTECH 컴퓨터공학과'})
CREATE (이상훈:instructor {name: '이상훈', college: '성균관대학교', career: '9년', position: '교수', organization: '성균관대학교 소프트웨어학과'})
CREATE (정수민:instructor {name: '정수민', college: '한양대학교', career: '6년', position: '강사', organization: '한양대학교 정보통신대학'})
CREATE (김지현:instructor {name: '김지현', college: '중앙대학교', career: '4년', position: '조교수', organization: '중앙대학교 디자인학부'})
CREATE (이재훈:instructor {name: '이재훈', college: '부산대학교', career: '11년', position: '부교수', organization: '부산대학교 전자공학부'})
CREATE (최민수:instructor {name: '최민수', college: '경희대학교', career: '3년', position: '강사', organization: '경희대학교 사이버보안학과'})


CREATE (파이썬 따라잡기:badge {name: '파이썬 따라잡기', level: '초급', learning_time: '10시간'})
CREATE (자바스크립트 마스터:badge {name: '자바스크립트 마스터', level: '중급', learning_time: '12시간'})
CREATE (웹 개발 전문가:badge {name: '웹 개발 전문가', level: '고급', learning_time: '15시간'})
CREATE (DB 기초:badge {name: 'DB 기초', level: '초급', learning_time: '8시간'})
CREATE (ML 초보:badge {name: 'ML 초보', level: '초급', learning_time: '20시간'})
CREATE (안드로이드 개발자:badge {name: '안드로이드 개발자', level: '중급', learning_time: '25시간'})
CREATE (클라우드 기초:badge {name: '클라우드 기초', level: '초급', learning_time: '18시간'})
CREATE (디자인 기초:badge {name: '디자인 기초', level: '초급', learning_time: '14시간'})
CREATE (IoT 초보ge9:badge {name: 'IoT 초보', level: '초급', learning_time: '22시간'})
CREATE (보안 기초:badge {name: '보안 기초', level: '초급', learning_time: '16시간'})


MATCH (l:lecture), (i:instructor)
WHERE l.instructor = i.name
CREATE (i)-[:TEACHES]->(l)

MATCH (l:lecture), (b:badge)
WHERE l.badge = b.name
CREATE (l)-[:HAS_BADGE]->(b)

MATCH (l:lecture), (k:knowledge)
WHERE l.name = k.reference_name
CREATE (l)-[:COVERS]->(k)
