DiscreteMath_class
==================


m).
 Konacno je m = M(jxi 􀀀 xj j; n).
Niz (xi) se konstruira pomocu neke funkcije f : Zn ! Zn od koje se trazi odredena
\slucajnost". U tu svrhu su dobri kvadratni polinomi, npr. f(x) = x2 + 1. Odabere se
neka pocetna vrijednost x0, npr. x0 = 2, a ostale vrijednosti se dobivaju kao iterirane
vrijednosti funkcije f, tj. xi+1 = f(xi). Jasno je da u beskonacnom nizu x0; x1; x2; : : :
koji poprima samo konacno mnogo vrijednosti, od nekog mjesta se taj niz mora poceti
periodicno ponavljati zbog xi+1 = f(xi).
Kako pronaci neki netrivijalni faktor m prirodnog broja n kada imamo konstruiran niz
(xi)? Ako bismo racunali M(jxi 􀀀 xj j; n) za sve i; j, to bi bilo jako neefikasno. Puno
bolje je racunati samo M(jx2i 􀀀 xij; n). Ova ideja se temelji na Floydovom algoritmu za
trazenje ciklusa. U tom slucaju za racunanje vrijednosti yi = x2i nije potrebno racunati
meduvrijednosti xi+1; xi+2; : : : ; x2i􀀀1, vec se racunanje odvija na sljedeci nacin:
xi = f(xi􀀀1) mod n;
yi = f
􀀀
f(yi􀀀1)

mod n:
Trazenje traje tako dugo dok M(jx2i 􀀀 xij; n) ne postane razlicita od 1. Ako je u tom
slucaju M(jx2i 􀀀 xij; n) 6= n, tada je M(jx2i 􀀀 xij; n) netrivijalni faktor od n. Ako pak je
M(jx2i 􀀀 xij; n) = n, tada algoritam nije uspio pronaci neki netrivijalni faktor prirodnog
broja n i u tom slucaju treba promijeniti funkciju f i pokusati ponovo sve iz pocetka s
novom funkcijom f. Standarno mozemo birati funkcije oblika f(x) = x2+c; c 2 Znf0;􀀀2g.
Uocite da algoritam nece uspijeti ukoliko je na ulazu prosti broj p jer ce u tom slucaju
uvijek biti M(jx2i 􀀀 xij; n) jednaka 1 ili p. Inace je algoritam vrlo efikasan na brojevima
koji imaju male proste faktore. Npr., prosti broj s desetak znamenki u decimalnom zapisu
je mali prosti broj, dok je za danasnja racunala prosti broj s 200 znamenki u decimalnom
zapisu veliki prosti broj.
Zadatak 5.
Implementirajte Pollardovu  metodu. Algoritam pocnite s funkcijom f(x) = x2 􀀀1. Ako
algoritam ne uspije pronaci netrivijalni faktor zadanog prirodnog broja n pomocu trenutne
funkcije f, tada neka odabere neku drugu funkciju oblika f(x) = x2 + c za neki slucajno
odabrani prirodni broj 0 < c < n 􀀀 2.
Jedno moguce ubrzanje Pollardove  metode bazira se na sljedecoj cinjenici:
Ako je M(a; n) > 1, tada je M(ab; n) > 1 za svaki b 2 N.
Stoga, umjesto da se u svakom koraku racuna M(jx2i 􀀀 xij; n), definira se varijabla z
kao produkt 100 uzastopnih clanova oblika jx2i 􀀀 xij modulo n i nakon toga se izracuna
M(z; n). Na taj nacin se najveca zajednicka mjera racuna tek nakon svakih 100 koraka.
Drugim rijecima, svakih 100 racunanja najvecih zajednickih mjera, u ovom slucaju zapravo
mijenjamo s 99 mnozenja modulo n i jednim racunanjem najvece zajednicke mjere, sto
3
pridonosi povecanju brzine izvodenja algoritma. S druge strane, u ovom slucaju je veca
vjerojatnost da se dogodi da je M(z; n) = n pa algoritam nece uspijeti naci netrivijalni
faktor broja n. U tom slucaju mozemo probati smanjiti broj 100, na primjer na 50, tj.
da svakih 50 koraka racunamo najvecu zajednicku mjeru i u slucaju neuspjeha ponovo
smanjiti broj 50 na pola i tako dalje redom. U najgorem slucaju ponovo cemo doci do
obicne Pollardove  metode.
Zadatak 6.
Implementirajte modiciranu Pollardovu  metodu za trazenje netrivijalnog faktora zada-
nog prirodnog broja n. Algoritam neka pocne s funkcijom f(x) = x2 􀀀 1 i neka nakon
svakih 100 koraka racuna najvecu zajednicku mjeru M(z; n). Ukoliko algoritam ne uspije
pronaci netrivijalni faktor broja n, tada se automatski krece ispocetka s novim korakom
racunanja najvecih zajednickih mjera M(z; n) koji je upola manji od prethodnog koraka
(u ovom slucaju svakih 50 koraka). U slucaju ponovnog neuspjeha, automatski se krece
ispocetka s upola manjim korakom racunanja najvecih zajednickih mjera M(z; n) od pret-
hodnog (u ovom slucaju svakih 25 koraka). Opcenito, u slucaju neuspjeha, algoritam
neka krene automatski ispocetka s upola manjim korakom racunanja najvecih zajednickih
mjera M(z; n) od prethodnog koraka. Ukoliko algoritam ne uspije pronaci netrivijalni fak-
tor broja n niti nakon sto dode do obicne Pollardove  metode (gdje se u svakom koraku
racuna najveca zajednicka mjera), tada algoritam bira novu funkciju f oblika f(x) = x2+c
za neki slucajno odabrani prirodni broj 0 < c < n 􀀀 2 i algoritam ponavlja ponovo istu
pricu s novom funkcijom f.
Pollardova p􀀀1 metoda. Ovo je takoder jedna specijalna metoda faktorizacije koja se
bazira na malom Fermatovom teoremu prema kojem je ap􀀀1  1 (mod p) za svaki prosti
broj p i prirodni broj a za koji je M(a; p) = 1. Tada je takoder am  1 (mod p) za svaki
visekratnik m broja p 􀀀 1. Iz toga slijedi am 􀀀 1  0 (mod p) pa zakljucujemo da je p
faktor od am􀀀1. Na posljednjem zakljucku se zapravo bazira ova metoda. Naime, ugrubo
receno, ukoliko zelimo pronaci neki netrivijalni faktor prirodnog broja n, tada gledamo
brojeve oblika at 􀀀 1 i provjeravamo da li neki od njih ima zajednicki faktor s n. Ukoliko
ima, uspjeli smo pronaci neki netrivijalni faktor broja n.
Pitamo se kako u prakticnoj implementaciji birati brojeve oblika at 􀀀 1. Postoji vise
varijanti, a mi cemo ovdje u opisu algoritma spomenuti jednu takvu varijantu koja ne
zahtijeva puno dodatne teorije. Najcesce se uzima a = 2 (mozemo pretpostaviti da je
n neparan broj jer iz svakog parnog broja lagano izlucimo njegov parni dio i svedemo
problem na neparni broj), a onda postoji vise varijanti na koje nacine mozemo birati
brojeve t.
U kojem slucaju je ova metoda uspjesnija od ostalih metoda? Zapravo sve ovisi o broju
p 􀀀 1. Prosti faktor p je mozda tesko pronaci, medutim p 􀀀 1 je potpuno drugaciji broj
od broja p. Ukoliko su svi prosti faktori broja p 􀀀 1 mali, tada ce ova metoda uspjeti
efikasno pronaci netrivijalni faktor zadanog broja n kojemu je p neki prosti faktor (koji
ne mora biti mali broj). Ako odaberemo dobar t, tada ce brojevi t i p 􀀀 1 imati puno
zajednickih faktora i upravo na dobrom odabiru broja t pociva efikasnost algoritma (jasno,
uz pretpostavku da su svi prosti faktori od p 􀀀 1 mali).
U nastavku slijedi opis jedne varijante algoritma. Neka je n zadani neparni prirodni broj
kojemu zelimo naci neki netrivijalni faktor. Stavimo da je a = 2. Za k 2 N gledamo
brojeve oblika xk =
􀀀
2k! 􀀀 1

mod n. U svakom koraku racunamo rk = M(xk; n). Ako je
4
rk 6= 1 i rk 6= n, tada je rk netrivijalni faktor broja n i algoritam zavrsava i vraca brojeve
rk i n
rk
. Ukoliko to nije slucaj, algoritam prelazi na sljedeci korak.
Zadatak 7.
Implementirajte opisanu Pollardovu p 􀀀 1 metodu. Za uspjesnu implementaciju potreban
je algoritam za modularno potenciranje, tj. efikasno racunanje izraza 2k! mod n. Python
vec sadrzi gotovu naredbu pow za ovaj problem koju slobodno koristite tako da ne morate
implementirati algoritam za modularno potenciranje.
Konacno, posljednja dva algoritma koje trebate implementirati se odnose na faktorizaciju
prirodnog broja.
Zadatak 8.
Implementirajte algoritam za faktorizaciju malih prirodnih brojeva koji je baziran na im-
plementiranom algoritmu u 2. zadatku. Ako n = p1
1 p2
2    pk
k faktorizacija prirodnog
broja n na proste faktore, tada algoritam na izlazu mora vratiti rjecnik
fp1 : 1; p2 : 2; : : : ; pk : kg:
Ako je n prosti broj, algoritam vraca rjecnik fn : 1g. Ako je n = 1, algoritam vraca prazni
rjecnik fg.
Zadatak 9.
Implementirajte algoritam za faktorizaciju prirodnog broja n koji je baziran na vec im-
plementiranim algoritmima u zadacima 2, 3, 6 i 8. U nastavku slijedi opis nacina rada
algoritma.
 Ako je n 6 1010, automatski se koristi implementirani algoritam u 8. zadatku.
 Ako je n > 1010, tada se koriste algoritmi implementirani u zadacima 3 i 6. Modi-
ficirana Pollardova  metoda sluzi da pronadete neki prosti faktor broja n, a Miller-
Rabinov test koristite za ispitivanje prostosti nekog broja. Pazite, Pollardova  me-
toda ne daje nuzno prosti faktor promatranog broja n, vec samo neki njegov faktor.
Na vama je da osmislite kako pomocu (modificirane) Pollardove  metode, algoritma
iz 2. zadatka i Miller-Rabinovog testa pronaci neki prosti faktor broja n. Nakon sto
algoritam pronade neki prosti faktor p1 zadanog broja n, tada ispituje koliko se puta
taj faktor nalazi u broju n, tj. racuna 1. Dobivene podatke zapisuje u rjecnik i
nastavlja dalje faktorizirati broj n
p
1
1
na gore vec opisani nacin. Nakon sto algoritam
pronade neki prosti faktor p2 broja n
p
1
1
, izracuna 2 i dobivene podatke spremi u
rjecnik. Dalje se nastavlja s faktorizacijom broja n
p
1
1 p
2
2
. I tako dalje redom. Ako
se dode do koraka u kojem dalje trebati nastaviti s faktorizacijom broj m 6 1010,
tada se algoritam automatski prebacuje na implementirani algoritam u 8. zadatku
pomocu kojeg se dovrsava faktorizacija.
Pazite da uvijek prije primjene Pollardove  metode provjerite da ju ne primjenjujete na
prostom broju jer na prostim brojevima ta metoda sigurno ne funkcionira. U slucaju da
algoritam ne uspijeva faktorizirati zadani prirodni broj n (dugo se izvodi), tada korisnik
sam prekida izvodenje algoritma. Sto znaci \algoritam se dugo izvodi"? Rijec \dugo"
moze svasta znaciti: deset minuta, dva sata, tri dana,. . .Na samom je korisniku da odluci
5
koliko ce vremena dati algoritmu za rad. Ukoliko algoritam uspije faktorizirati zadani
prirodni broj n, tada na izlazu vraca rjecnik kako je to vec opisano u 8. zadatku.
Na kraju jos nekoliko prakticnih zadataka na kojima cete testirati svoje implementirane
algoritme.
Zadatak 10.
U svakoj od datoteka broj1.txt, broj2.txt, broj3.txt, broj4.txt, broj5.txt,
broj6.txt, broj7.txt, broj8.txt nalazi se spremljen po jedan prirodni broj. Na sva-
kom od tih brojeva testirajte svoje implementirane algoritme iz zadataka 2.-9. Ukoliko se
u nekom slucaju neki od algoritama dulje izvodi, sami procijenite da li ce uspjeti i koliko
mu vremena treba da obavi posao (dajte svakom barem desetak minuta sanse, ili vise ili
mozda manje, ovisno vec o vasim procjenama, teoretskom znanju o uspjesnosti pojedinog
algoritma, ali isto tako i o kvaliteti vasih implementacija).
Zadatak 11.
U svakoj od datoteka P1.txt i P2.txt nalazi se spremljen po jedan prirodni broj. Ispitajte
da li je neki od tih brojeva prost. U slucaju da broj nije prost, pokusajte pronaci njegovu
faktorizaciju na proste faktore pomocu svojih implementiranih algoritama.
Zadatak 12.
Vas poslodavac vas zeli poslati na jedan tajni zadatak. Vi ste jedan od njegovih najboljih
tajnih agenata. Medutim, za ovaj zadatak je potrebno imati i mnoge vjestine dobrog mate-
maticara. Naime, neprijatelj postaje sve opasniji i matematicki obrazovaniji, vremena je
sve manje, a sudbina svijeta ovisi o vasem znanju o RSA kriptosustavu. Neprijatelj sifrira
vazne poruke upravo RSA kriptosustavom. Stoga ste dobili probni zadatak da pokusate
razbiti RSA sifrat ciji je javni kljuc spremljen u datotekama N0.txt i E.txt. Sifrat je
spremljen u datoteci kod0.txt. Dajte sve od sebe jer ako Vi ne uspijete, poslodavac ce
poslati nekog drugog na tajni zadatak.
Zadatak 13.
Opravdali ste status najboljeg tajnog agenta i uspjesno rijesili problem iz prethodnog za-
datka. No, sada ste na ozbiljnom tajnom zadatku. Od vas se puno ocekuje. Uspjeli
ste neprijatelju uci u trag i dokopati se sifrirane poruke koja je spremljena u datoteci
kod1.txt. Takoder, saznali ste da je sifrat sifriran javnim kljucem koji je spremljen u
datotekama N1.txt i E.txt. U njemu je vazna poruka o tome na koje mjesto trebate doci
kako biste iznenadili neprijatelja i pokupili daljnje vazne informacije. Kako je neprija-
telj bio neoprezan prilikom sifriranja i potcijenio vase matematicko znanje, to vama daje
prostora da razbijete taj sifrat i ukradete mu vazne informacije tako da odete na mjesto
sastanka koje se spominje u sifriranoj poruci. Dajte sve od sebe.
Zadatak 14.
Vas poslodavac je prezadovoljan s vama. Uspjesno ste prebrodili sve prepreke i do sada
razbili sve sifrirane poruke. Medutim, to nije kraj. Neprijatelj ipak ne posustaje unatoc
unutarnjim nesuglasicama zbog neuspjeha. Dosli ste na los glas u neprijateljskim krugo-
vima i sada prate svaki vas korak. Vi ste svjesni toga, ali svaka vasa pogreska moze vas
skupo kostati. Ovaj put oni vas planiraju iznenaditi na jednom od odredista koja morate
posjetiti. No, ne znate na kojem vas tocno odredistu namjeravaju zaskociti. Neprijatelj i
6
dalje hrabro komunicira preko sifriranih poruka ne znajuci za vase hakerske sposobnosti
koje su na zavidnom nivou. Ponovo ste se dokopali njihove sifrirane poruke koju su slali
preko nesigurnog komunikacijskog kanala. U toj poruci se izmedu ostalog spominje mjesto
na kojem vas namjeravaju napasti. Zelite li se spasiti, ne preostaje vam nista drugo,
nego da razbijete sifriranu poruku koje ste se docepali. Sifrirana poruka je spremljena u
datoteci kod2.txt. Takoder, saznali ste da je sifrirana javnim kljucem koji je spremljen
u datotekama N2.txt i E.txt. Sto jos reci? Vasa sigurnost je u pitanju. To je valjda
dovoljna motivacija za razbijanje sifrata.
Zadatak 15.
Na kraju, nakon svih vasih uzbudenja u ulozi tajnog agenta, ceka vas samo jos jedan
zadatak. Posljednji sifrat kojeg trebate razbiti. Do sada ste stekli vec puno iskustava pa ne
bi to trebao biti neki problem. Sifrat je spremljen u datoteci kod3.txt, a sifriran je javnim
kljucem koji je spremljen u datotekama N3.txt i E.txt. Pritom su datoteke kod3.txt
i N3.txt spremljene u sifriranu datoteku kod3N3.zip. Sifru za zip datoteku ste saznali
u prethodnim zadacima. Zelite li saznati zavrsetak price, prionite na posao. Sigurno ste
jako znatizeljni, sto se na kraju dogodilo.
Dodatne upute. Sve implementacije u prvih devet zadataka treba napraviti u program-
skom jeziku Python 2.x kako je vec ranije receno. Pritom ne smijete koristiti nikakve
eventualne gotove funkcije koje mozda automatski rjesavaju zadani problem kako biste
pomocu njih izbjegnuli svoju implementaciju (osim onoga sto je eksplicitno navedeno da
se eventualno smije koristiti). No, kako bi se vidjelo da ste zaista svoje algoritme tes-
tirali na preostalim prakticnim zadacima, sve testove treba napraviti unutar IPython
notebooka. Dakle, svoje implementacije funkcija spremite u jednu py datoteku (ta da-
toteka neka ne bude izvrsna datoteka, nego neka samo sadrzi implementirane funkcije).
Tu datoteku ucitajte u IPython notebook kako biste unutar njega mogli koristiti svoje
implementirane funkcije. Isto tako, sve preostale prilozene datoteke u kojima su sprem-
ljeni odredeni brojevi takoder ucitajte u svoj notebook pomocu Python funkcija za rad s
datotekama. Dakle, nemojte copy-pejstati brojeve iz datoteka u notebook, nego ih preko
gotovih Python funkcija za rad s datotekama ucitajte u notebook, pretvorite u odgo-
varajuci format i spremite u neke varijable preko kojih cete pristupati tim brojevima.
Pomocu gotove IPython funkcije %time mjerite koliko je vremena potrebno pojedinom
algoritmu da se izvrsi na pojedinom broju.
Sto se tice rjesavanja zadnja cetiri zadatka u kojima trebate razbiti RSA sifrate, princip
rjesavanja je sljedeci. Za razbijanje sifrata trebate koristiti svoje implementirane Python
funkcije. Dakle, vas postupak dobivanja tajnog dijela kljuca mora biti jasno vidljiv u
IPython notebooku. Samo desifriranje obavite pomocu Python programa guiRSA.py.
Nacin funkcioniranja tog programa opisan je u datoteci rsa.pdf. Nakon sto razbijete
sifrat, pomocu Python funkcija za rad s datotekama ucitajte desifrirani tekst iz datoteke
u IPython notebook.
Napomena. Program guiRSA.py je zapravo prilagoden za rad na ubuntu linuxu. Ova
implementacija nece ispravno raditi na windowsima.
Bodovanje. Zadaca nosi maksimalno 5 bodova, a ugrubo je princip bodovanja sljedeci:
7
rijeseni zadaci broj bodova
1., 2., 8. 1
3., 4., 7. 1
5., 6., 9. 1
12., 13., 14., 15. 1
IPython notebook 1
Pritom se pretpostavlja da ukoliko rijesite samo neke od prvih devet zadataka da svakako
svoje funkcije koje ste napravili testirate na 10. i 11. zadatku ukoliko se u tim dvama
zadacima trazi testiranje tih funkcija. Na primjer, ako rijesite 1., 2. i 8. zadatak, tada je
u taj 1 bod ukljuceno i testiranje tih funkcija na 10. i 11. zadatku, ukoliko to ti zadaci
zahtijevaju. Slicno je i za sve ostale kombinacije. Na primjer, ako ste rijesili samo 3. i 5.
zadatak, tada je u bodovanje ukljuceno i testiranje tih funkcija na 10. i 11. zadatku. Jedan
bod dobivate za sam izgled IPython notebooka da sve bude uredno formatirano, jasno
napisano, slicno IPython materijalima na moodlu. Na primjer, ukoliko zelite napisati neki
svoj komentar, nemojte tekst direktno pisati u input celiju, vec pretvorite celiju u tekst
format. Radi lakse orijentacije, u datoteci primjer.html je pokazano testiranje funkcija
na jednom broju.
Moodle. Na moodle treba predati sljedece datoteke:
 ipynb datoteku { datoteka za IPython notebook
 html datoteku { html verzija ipynb datoteke
 py datoteku { datoteka u kojoj su vasi implementirani algoritmi
 sve ostale datoteke i direktorije koji su potrebni kod izvrsavanja pojedinih naredbi
u IPython notebooku ili kod citanja html datoteke.
Najbolje je da sve spomenute datoteke i direktorije spremite u jednu zip datoteku i nju
onda predate na moodle.
Napomena. Vasa zadaca se bude pregledavala na linuxu pa se preporuca koristenje
tog operacijskog sustava prilikom izrade ove zadace. Ukoliko ipak radite na windowsima,
molimo vas da na kraju testirate svoju zadacu na linuxu prije nego sto ju predate na
moodle. Imajte na umu da se vasa zadaca boduje prema tome koliko dobro radi na
linuxu.
