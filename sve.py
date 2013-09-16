
import random;
import gmpy;
from gmpy import mpz;
from gmpy import gcd;
import math;
from math import sqrt

#zad1
#nzm

q=[];
def NZM(a,b):
    if(b==0):
        return a;
    else:
        d=a%b;
        if d!=0:
            q.append((a-d)/b);
        return NZM(b,d);

def rjesiKongruenciju(a,b,n):
    mjera=NZM(n,a);
    rez = [0,1];
    rjesenja=[];
    if mjera == 1:
        print "Kongruencija ima jedinstveno rjesenje!";
        for i in q:
            rez.append(rez[-1]*(-i)+rez[-2]);
        x = (rez[-1]*b) % n;
        print "Rjesenje kongruencije je x = ",x
        return x;
    if mjera != 1 and b%mjera == 0:
        print "Kongruencija ima vise rjesenja";
        print 'Kongruencija nakon skracivanja s ',mjera,':\n', (a/mjera) ,'x = ' ,(b/mjera) , ' (mod ',(n/mjera) ,')';
        for i in q:
            print i
            rez.append(rez[-1]*(-i)+rez[-2]);

        x = (rez[-1]*(b/mjera)) % (n/mjera);
        print 'Sva rjesenja kongruencije su dana s \n xk = ' + repr(x) + ' + ' + repr(n/mjera) + 'k';
        print "Rjesenja kongruencije:\n";
        for i in range(0,mjera):
            rjesenja.append(x+(n/mjera)*i);
            print 'x' + repr(i) + ' = ' + repr(rjesenja[i]);
        return rjesenja;
    if mjera != 1 and b%mjera != 0:
        print "Kongruencija nema rjesenja!";
        return 0;
#zad2
#ispitivanje prostosti

def provjeraProstosti(n):
    granica = int(gmpy.ceil(gmpy.sqrt(n)));
    i=2;
    while(i<granica+1):
        if n % i == 0:
            return i;
        i+=1;
    return 1;
##
###zad 3 Miller-Rabin

prosti=[];
for a in range(2,200):
    if gmpy.is_prime(a):
        prosti.append(a);

def millerRabProlaz(a,s,d,n):
        potencija_A = pow(a, d, n)
        if potencija_A == 1:
            return True
        for i in xrange(s - 1):
            if potencija_A == n - 1:
                return True
            potencija_A = (pow(potencija_A,2)) % n
        return potencija_A == n-1

def millerRab(n):
    if n % 2 == 0 or n < 200 and n not in prosti:
        return False
    if n < 200 and n in prosti:
        return True
    else:
        d = n - 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
        for repeat in xrange(20):
            a = 0
            while a == 0:
                a = random.randrange(n)
            if not millerRabProlaz(a, s, d, n):
                return False
        return True

###zadatak 4 fermat

def fermat(n):
    if(n%2==0):
        print "Molimo unesite neparni broj."
    else:
        x1=gmpy.ceil(gmpy.sqrt(mpz(n)));
        #x1 =gmpy2.isqrt(n);
        #yi= xi^2-n <--check if its potpuni kvadrat
        y = ((x1*x1)) - n
        while not potpuniKvadrat(y):
            x1 += 1
            y = (x1*x1) - n
        a1 = x1 + gmpy.sqrt(mpz(y))
        a2 = x1 - gmpy.sqrt(mpz(y))
        return int(a1), int(a2) 

def potpuniKvadrat(n):
    if(n<=0):
        return False;
    korijen = gmpy.sqrt(mpz(n))
    #1 % 1 == 0 <-- potpuni kvadrat
    #1.2 %1 !=0 <-- fail
    if (korijen % 1 == 0):
        return True;
    else:
        return False;

###zadatak 5 Pollardova p metoda

def pollard(broj,c=-1):
    x = random.randint(1, broj-1);
    y = x;
    d = 1;
    z=1;
    if broj%2==0:
            return 2;
    if broj==1:
        return 1;
    if broj<=0:
        return "Unesite prirodan broj"
    if(c==-1):
        while d==1:
            #f(x)
            x = ((x*x)%broj+c)%broj;
            #f(y)
            y = ((y*y)%broj+c)%broj;
            #f(f(y))
            y = ((y*y)%broj+c)%broj;
            d=gcd(abs(x-y),broj);
            if (d==broj):
                c = random.randint(1, broj-1);
                pollard(broj,c);
            elif(d!=broj and d!=1):
                return d;
    if(c!=-1):
        while d==1:
            #f(x)
            x = ((x*x)%broj+c)%broj;
            #f(y)
            y = ((y*y)%broj+c)%broj;
            #f(f(y))
            y = ((y*y)%broj+c)%broj;
            d=gcd(abs(x-y),broj)
            if(d==broj):
                break;
        return d;

###zadatak 6 improved Pollardova p metoda

def improvedPollard(broj,c=-1,counter=100,zastavica=False):
    random.seed();
    x = random.randint(1, broj-1);
    x=mpz(x)
    y = x;
    d = mpz(1);
    z=mpz(1);
    korak=counter;
    # ako je paran broj vrati 2 kao prost faktor
    if broj%2==0:
            return 2;
    if broj<=0:
        return "Unesite prirodan broj"
    #prvi prolaz za funkcijom x^2 -1
    if(c==-1):
        while d==1:
            for i in range(counter):
                #f(x)
                x = ((x*x)+c)%broj;
                #f(y)
                y = ((y*y)+c)%broj;
                #f(f(y))
                y = ((y*y)+c)%broj;
                #produkt modula
                z=abs(z*(x-y))%broj;
            #nzm produkta i n
            d=gmpy.gcd(mpz(z),mpz(broj));
            #ako je korak>1 a jos nije nasao broj
            if((d==1 or d==broj) and c==-1 and korak>1):
                d=improvedPollard(broj,c,korak/2);
            #ako je korak 1 a nije nasao broj
            elif((d==1 or d==broj) and c==-1 and korak==1):
                c = random.randint(1, broj-1);
                d=improvedPollard(broj,c,korak);
            #nasao je broj
            else:
                return d;
        #za ispis prilikom vracanja iz rekurzije
        return d;
    #drugi prolaz
    if(c!=-1):
        while (d==1):
            for i in range(counter):
                #f(x)
                x = ((x*x)+c)%broj;
                #f(y)
                y = ((y*y)+c)%broj;
                #f(f(y))
                y = ((y*y)+c)%broj;
                #produkt modula
                z=abs(z*(x-y))%broj;
            #nzm produkta i n
            d=gmpy.gcd(mpz(z),mpz(broj));
            ##ako je korak>1 a jos nije nasao broj
            if (korak>1 and (d==1 or d==broj or d==None)):
                #smanji korak za 1/2
                d= improvedPollard(broj,c,korak/2);
            #ako je korak 1, prvi prolaz, a nije nasao broj promijeni c
            elif (korak==1 and (d==1  or d==None) and not zastavica):
                c = random.randint(1, broj-1);
                d= improvedPollard(broj,c,1,True);
            #nasao je broj | upisan je prost broj
            elif(zastavica and d==broj):
                return d;
        #za ispis prilikom vracanja iz rekurzije
        return d;

###zadatak 7 pollard ro -1

def pollardRo1(n,k=0,zastavica=0):
    a=2;
    if(n%2==0):
        parniFaktor=1;
        while(is_even(n)):
              n=n/2;
              parniFaktor*=2;
        print "Parni faktor:",parniFaktor
    if(k<=0):
        k=random.randint(1, n);
    i=0;
    if(gmpy.is_prime(n)):
       return n;
    if(gmpy.gcd(a,n)!=1):
        return a;
    while i<k:
        i+=1;
        x=pow(a,i,n)
        
        r=gcd(x-1,n);
        if(r==1):
            zastavica+=1
        if(r!=1 and r!=n):
            return int(r),int((n/r));
    return pollardRo1(n,k+1,zastavica); 
            
###zad 8 faktorizacija malih  brojeva e N

def faktorizacija(n):
    faktori = {};
    if n == 1:
        return faktori;
    rezultat = millerRab(n);
    if rezultat == True:
        #vraca {n:1}
        faktori[n] = 1;
        return faktori;
    else:
        i = 2;
        brojac = 1;
        while i <= n:
            if n % i == 0:
                n /= i;
                if faktori.has_key(i):
                    brojac += 1;
                    faktori[i] = brojac;
                else:
                    brojac = 1;
                    faktori[i] = brojac;
                    
            else:
                i += 1;
        return faktori;
                     
###zad 9
###algoritam za faktorizacija brojeva

def faktorizacijaAlgoritam(n):
    #kod svakog ulaska u rekurziju definiraj novi rjecnik pa tijekom vracanja
    #iz rekurzije appendaj dio po dio krajnjem rijecniku
    rjecnik={};
    broj=n;    
    if(n<=pow(10,10)):
        broj=faktorizacija(n);
        rjecnik.update(broj);
        return rjecnik;
    else:
        #tek ako je prost broj racunaj sa pollardom
        if(millerRab(n)==False):
            #izracunaj jedan faktor
            broj=improvedPollard(n);
            #trazi faktor dok ne bude prost broj
            while(millerRab(broj)==False):
                ct = random.randint(1, 100);
                c = random.randint(1, broj-1);
                broj=improvedPollard(n,c,ct);
            #taj faktor se sigurno nalazi jednom u n
            brojFaktora=1;
            #podjeli n sa faktorom
            rezultat=n/broj;
            #pogledaj koliko jos tih faktora ima u  broju n (tj rezultatu)
            while not(rezultat % broj):
                brojFaktora+=1;
                rezultat=rezultat/broj
            #zapisi nadjeni faktor i broj njegovog ponavljanja
            rjecnik[broj]=brojFaktora
            #izracunaj ostale faktore sa ostatkom
            rjecnik.update(faktorizacijaAlgoritam(rezultat));
        else:
            rjecnik[broj]=1;
    #vrati rjecnik
    return rjecnik;
