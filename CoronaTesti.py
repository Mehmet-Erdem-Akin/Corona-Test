# CORONA MISINIZ ? #
while True:
    print("-------------------------------------------------------------------------------------------------------")
    print(" lütfen sorularımızı ( yok (0) , nadiren (1) , bazen (2) , sık (3) , şiddetli (4) ) olarak belirtiniz")
    print("çıkmak için (q) basınız ")
    print("-------------------------------------------------------------------------------------------------------")

    ates = input("ateşiniz var mı ? : ")
    
    if ates == "q":
        print("Testten çıkış yaptınız")
        break 

    yorgunluk = input("yorgunluğunuz var mı ) : ")
    kuru_oksuruk = input("kuru öksürük var mı ) : ")
    solunum_zorlugu = input("solunum_zorlugu var mı ) : ")
    oksuruk = input("oksuruk var mı ) : ")
    agri = input("agri var mı ) : ")
    hapsirma = input("hapsirma var mı ) : ")
    burun_akintisi = input("burun_akintisi var mı ) : ")
    burun_tikanikligi = input("burun_tikanikligi var mı ) : ")
    gozlerde_sulanma = input("gozlerde_sulanma var mı ) : ")
    bogaz_agrisi = input("bogaz_agrisi var mı ) : ")
    ishal = input("ishal var mı ) : ")

    if ates == "3" and yorgunluk == "3" and kuru_oksuruk == "3" and solunum_zorlugu == "4" and oksuruk == "3" and agri == "2" and (hapsirma == "0" or hapsirma == "1" or hapsirma == "2" or hapsirma == "3" or hapsirma == "4") and burun_akintisi == "2" and (burun_tikanikligi == "0" or burun_tikanikligi == "1" or burun_tikanikligi == "2" or burun_tikanikligi == "3" or burun_tikanikligi == "4") and (gozlerde_sulanma == "0" or gozlerde_sulanma == "1" or gozlerde_sulanma == "2" or gozlerde_sulanma == "3" or gozlerde_sulanma == "4") and bogaz_agrisi == "2" and ishal == "2":
        print(" üzgünüz corona'ya yakalanmışsınız kimseyle temas etmeyin ve hemen 184'ü arayın !!!")

    elif ates == "1" and yorgunluk == "2" and kuru_oksuruk == "0" and solunum_zorlugu == "0" and oksuruk == "0" and agri == "1" and hapsirma == "3" and burun_akintisi == "0" and burun_tikanikligi == "3" and gozlerde_sulanma == "0" and bogaz_agrisi == "3" and ishal == "0":
        print(" geçmiş olsun (soğuk algınlığı / nezle)'ye yakalanmışsınız. Bol bol C vitamini , nane limon tüketiniz. ")

    elif ates == "3" and yorgunluk == "3" and kuru_oksuruk == "3" and solunum_zorlugu == "0" and oksuruk == "2" and agri == "3" and hapsirma == "2" and burun_akintisi == "2" and burun_tikanikligi == "2" and gozlerde_sulanma == "0" and bogaz_agrisi == "2" and ishal == "1":
        print("geçmiş olsun gribe yakalanmışsınız !!!. Acilen istirahat edip dinleniniz. Durumunuzun düzelmemesi durumunda tekrar doktorunuza başvurunuz. ")

    elif ates == "0" and yorgunluk == "2" and kuru_oksuruk == "2" and solunum_zorlugu == "2" and oksuruk == "2" and agri == "0" and hapsirma == "3" and burun_akintisi == "3" and burun_tikanikligi == "3" and gozlerde_sulanma == "3" and bogaz_agrisi == "0" and ishal == "0":
        print("geçmiş olsun , Alerji'ye yakalanmışsınız. Lütfen doktorunuza danışıp gerekli testleri uygulayın ")

    else:
        print("hasta değilsiniz, geçmiş olsun :) ")

