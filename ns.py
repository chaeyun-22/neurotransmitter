import csv

neu_trans = []
'''
class Nervous_disease():
    
    def __init__(self, name, neurotransmitter, concentration):
        self.name = name
        self.neurotransmitter = neurotransmitter
        self.concentration = concentration

    def patient_info(self):
        print(f"환자 이름: {self.name}, 신경 전달 물질 종류: {self.neurotransmitter}, 수치: {self.concentration}")
'''
class Patient:
   
    def __init__(self, name, neurotransmitter, concentration):
        self.name = name
        self.neurotransmitter = neurotransmitter
        self.concentration = float(concentration)

    def patient_info(self):
        print(f"환자 성함: {self.name}, 신경전달물질 종류: {self.neurotransmitter}, 수치: {self.concentration}")
        analysis = Disease_analysis(self)
        level = analysis.analyze()
        analysis.prescribe(self.neurotransmitter, level)

class Disease_analysis:
    global neu_trans
   
    def __init__(self, patient):
        self.patient = patient

    def analyze(self):
        neu_trans = self.patient.neurotransmitter
        concen = self.patient.concentration

        if neu_trans == "도파민":
            low, high = 0.03, 0.07
        elif neu_trans == "세로토닌":
            low, high = 101, 283
        elif neu_trans == "노르에피네프린":
            low, high = 70, 170
        elif neu_trans == "GABA":
            low, high = 0.5, 3.0
        elif neu_trans =="글루탐산":
            low, high = 40, 80
        else:
            print("해당 신경전달물질의 정상 수치를 알 수 없습니다.")
            return
       
        if concen < low:
            print(f"{neu_trans} 수치가 너무 낮습니다. (정상 범위: {low}~{high})")
            return "low"
        elif concen > high:
            print(f"{neu_trans} 수치가 너무 높습니다. (정상 범위: {low}~{high})")
            return "high"
        else:
            print(f"{neu_trans} 수치가 정상 범위에 있습니다. (정상 범위: {low}~{high})")
            return 0
        
        return neu_trans

    def prescribe(self, neu_trans, level):
        if neu_trans == "도파민":
            if level == "low":
                print("추정되는 질병: 파킨슨병, 우울증")
                print("처방약: L-도파, 프라미펙솔")
            elif level == "high":
                print("추정되는 질병: 조현병, 충동조절장애")
                print("처방약: 리스페리돈, 올란자핀")
            else:
                print("수치가 정상이므로 처방할 약이 없습니다.")
        elif neu_trans == "세로토닌":
            if level == "low":
                print("추정되는 질병: 우울증, 불안장애")
                print("처방약: 플루옥세틴, 설트랄린")
            elif level == "high":
                print("추정되는 질병: 세로토닌 증후군")
                print("처방약: 사이프로헵타딘")
            else:
                print("수치가 정상이므로 처방할 약이 없습니다.")
        elif neu_trans == "노르에피네프린":
            if level == "low":
                print("추정되는 질병: 무기력, 집중력 저하")
                print("처방약: 벤라팍신, 덜록세틴")
            elif level == "high":
                print("추정되는 질병: 불안, 고혈압")
                print("처방약: 프로프라놀롤, 클로니딘")
            else:
                print("수치가 정상이므로 처방할 약이 없습니다.")
        elif neu_trans == "GABA":
            if level == "low":
                print("추정되는 질병: 불안장애, 불면증")
                print("처방약: 로라제팜, 가바펜틴")
            elif level == "high":
                print("추정되는 질병: 졸림, 무기력")
                print("처방약: 자극제(카페인 등) 신중히 사용")
            else:
                print("수치가 정상이므로 처방할 약이 없습니다.")
        elif neu_trans == "글루탐산":
            if level == "low":
                print("추정되는 질병: 인지 기능 저하, 피로감")
                print("처방약: NMDA 작용제 (연구중)")
            elif level == "high":
                print("추정되는 질병: 간질, 신경 독성")
                print("처방약: 메만틴, 토피라메이트")
            else:
                print("수치가 정상이므로 처방할 약이 없습니다.")

patient_list = []
nervous_disease = ["도파민", "세로토닌", "노르에피네프린", "GABA", "글루탐산"]

def ns_disease(filename):
    global patient_list

    file = open(filename, "r", encoding="utf-8-sig")
    patient = csv.reader(file)

    header = next(patient)
    print(header)

    for line in patient:
        name, neurotransmitter, concentration = line
        patient_obj = Patient(name, neurotransmitter, concentration)
        patient_list.append(patient_obj)
    
    for p in patient_list:
        p.patient_info()

    file.close()

def add_patient():
    global patient_list

    name = (input("환자 성함: "))
    neurotransmitter = (input("신경전달물질 종류: "))

    if neurotransmitter not in nervous_disease:
        print("해당 신경전달물질을 비교할 수 없습니다.")
        return
    concentration = int(input("혈장 내 수치: "))
    new_patient = Patient(name, neurotransmitter, concentration)
    new_patient.patient_info()

    patient_list.append(new_patient)
    return neurotransmitter


def save_patient(filename):
    file = open(filename, "w", newline="", encoding="utf-8-sig")
    writer =csv.writer(file)

    writer.writerow(["name", "neurotransmitter", "concentration"])

    for p in patient_list:
        writer.writerow([p.name, p.neurotransmitter, p.concentration])

    print("파일이 업데이트 되었습니다.")
    file.close()

ns_disease("patient_list.csv")
print("\n--- 새로운 환자---")
neuro = add_patient()
if neuro in patient_list:
    save_patient("patient_list.csv")