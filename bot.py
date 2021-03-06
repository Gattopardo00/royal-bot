# -*- coding: utf-8 -*-
import json
import time
import filemanager
import telegram
import steam
import random
import osu
import lol
import discord

# Elenco di username dei membri della RYG
royalgames = json.loads(filemanager.readfile("db.json"))

# Stringa dove mettere l'elenco di champion di lol gratuiti
lolfreestring = str()

random.seed()


# Spostiamo qui le funzioni del bot, così è un po' più leggibile
def wow():
    print("@" + username + ": WOW!")
    telegram.sendmessage("Wow. Impressionante.", sentin, source)


def ahnonlosoio():
    print("@" + username + ": /ahnonlosoio")
    # Rispondi con Ah, non lo so nemmeno io.
    telegram.sendmessage("Ah, non lo so nemmeno io!", sentin, source)


def ciaostefanino():
    print("@" + username + ": /ciaostefanino")
    # Rispondi salutando Stefanino.
    telegram.sendmessage("Ciao Stefanino!", sentin, source)


def ciaoruozi():
    print("@" + username + ": /ciaoruozi")
    # Ciao Ruozi.
    if username.lower() == "ruozir":
        telegram.sendmessage("Ciao me", sentin, source)
    else:
        telegram.sendmessage("Ciao Ruozi", sentin, source)


def potatogift():
    telegram.senddocument("BQADAgADHwQAAh8GgAEmS1UU1zyaLQI", sentin, source)


def playing():
    print("@" + username + ": /playing")
    # Informa Telegram che il messaggio è stato ricevuto e visualizza Royal Bot sta scrivendo.
    telegram.sendchataction(sentin)
    cmd = text.split(" ")
    # Se è stato specificato un AppID...
    if len(cmd) >= 2:
        n = steam.getnumberofcurrentplayers(cmd[1])
        # Se viene ricevuta una risposta...
        if n is None:
            telegram.sendmessage(chr(9888) + " L'app specificata non esiste!", sentin, source)
        else:
            telegram.sendmessage(
                'In questo momento, ' + str(n) + ' persone stanno giocando a [' + cmd[1] +
                '](https://steamdb.info/app/' + cmd[1] + '/graphs/)', sentin, source)
    else:
        telegram.sendmessage(chr(9888) + ' Non hai specificato un AppID!\n'
                                         'La sintassi corretta è /playing <AppID>.', sentin, source)


def ehoh():
    print("@" + username + ": /ehoh")
    # Rispondi con Eh, oh. Sono cose che capitano.
    telegram.sendmessage("Eh, oh. Sono cose che capitano.", sentin, source)


def saldi():
    print("@" + username + ": /saldi")
    # Visualizza il link di isthereanydeal con i saldi di un gioco.
    # Informa Telegram che il messaggio è stato ricevuto e visualizza Royal Bot sta scrivendo.
    telegram.sendchataction(sentin)
    cmd = text.split(" ", 1)
    if len(cmd) == 2:
        telegram.sendmessage(
            'Visualizza le offerte di '
            '[' + cmd[1] + '](https://isthereanydeal.com/#/search:' + cmd[1].replace(' ', '%20') +
            ";/scroll:%23gamelist).", sentin, source)
    else:
        telegram.sendmessage(chr(9888) +
                             " Non hai specificato un gioco!"
                             "[Visualizza tutte le offerte]"
                             "(https://isthereanydeal.com/#/search:.;/scroll:%23gamelist).",
                             sentin, source)


def sbam():
    print("@" + username + ": /sbam")
    # Manda l'audio contenente gli sbam di tutti i membri Royal Games.
    telegram.senddocument('BQADAgADBwMAAh8GgAGSsR4rwmk_LwI', sentin)


def osucmd():
    print("@" + username + ": /osu")
    # Visualizza il punteggio più recente di osu!
    # Informa Telegram che il messaggio è stato ricevuto.
    telegram.sendchataction(sentin)
    # Trova il nome utente specificato
    cmd = text.split(' ', 1)
    # Se è stato specificato un nome utente
    if len(cmd) >= 2:
        # Trova la modalità
        # 0 = osu!
        # 1 = osu!taiko
        # 2 = osu!catch
        # 3 = osu!mania
        cmd = text.split(' ', 2)
        # Se è stata specificata una modalità
        if len(cmd) >= 3:
            # Modalità specificata
            mode = int(cmd[2])
        else:
            # Imposta la modalità a osu!
            mode = 0
        # Prova a mandare una richiesta ai server di osu per l'ultima canzone giocata
        try:
            r = osu.getuserrecent(cmd[1], mode)
        # Se la funzione restituisce un errore, riferisci su Telegram l'errore e previeni il crash.
        except NameError:
            telegram.sendmessage(chr(9888) + " Errore nella richiesta ai server di Osu!", sentin,
                                 source)
        # Se tutto va bene, continua!
        else:
            # Se ci sono delle mod attive...
            if "enabled_mods" in r:
                mods = osu.listmods(r['enabled_mods'])
            else:
                mods = ""
            # Specifica cosa vuole dire il grado F e il grado X
            if r['rank'] == 'F':
                r['rank'] = 'Failed'
            elif r['rank'] == 'X':
                r['rank'] = 'Unranked'
            if mode == 0:
                # Visualizza le informazioni relative alla modalità osu!
                telegram.sendmessage("*osu!*\n"
                                     "[Beatmap {0}](https://osu.ppy.sh/b/{0})\n"
                                     "*{1}*\n"
                                     "{2}\n"
                                     "*Punti*: {3}\n"
                                     "*Combo* x{4}\n"
                                     "*300*: {5}\n"
                                     "*100*: {6}\n"
                                     "*50*: {7}\n"
                                     "*Awesome*: {8}\n"
                                     "*Good*: {9}\n"
                                     "*Miss*: {10}"
                                     .format(r['beatmap_id'],
                                             r['rank'],
                                             mods,
                                             r['score'],
                                             r['maxcombo'],
                                             r['count300'],
                                             r['count100'],
                                             r['count50'],
                                             r['countgeki'],
                                             r['countkatu'],
                                             r['countmiss']), sentin, source)
            elif mode == 1:
                # Visualizza le informazioni relative alla modalità osu!taiko
                telegram.sendmessage("*osu!taiko*\n"
                                     "[Beatmap {0}](https://osu.ppy.sh/b/{0})\n"
                                     "*{1}*\n"
                                     "{2}\n"
                                     "*Punti*: {3}\n"
                                     "*Combo* x{4}\n"
                                     "*Great*: {5}\n"
                                     "*Good*: {6}\n"
                                     "_Large_ *Great*: {7}\n"
                                     "_Large_ *Good*: {8}\n"
                                     "*Miss*: {9}"
                                     .format(r['beatmap_id'],
                                             r['rank'],
                                             mods,
                                             r['score'],
                                             r['maxcombo'],
                                             r['count300'],
                                             r['count100'],
                                             r['countgeki'],
                                             r['countkatu'],
                                             r['countmiss']), sentin, source)
            elif mode == 2:
                # TODO: Cos'è successo qui?
                # Visualizza le informazioni relative alla modalità osu!catch
                telegram.sendmessage("*osu!catch*\n"
                                     "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                         'beatmap_id'] +
                                     ")\n*" + r['rank'] + "*\n" + mods +
                                     "\n*Punti*: " + r['score'] + "\n"
                                                                  "*Combo* x" + r['maxcombo'] + "\n"
                                                                                                "*Fruit*: " +
                                     r['count300'] + "\n"
                                                     "*Droplet* _tick_: " + r['count100'] + "\n"
                                                                                            "*Droplet* _trail_: " +
                                     r['count50'] + "\n"
                                                    "*Miss*: " + r['countmiss'], sentin, source)
            elif mode == 3:
                # TODO: Cos'è successo qui?
                # Visualizza le informazioni relative alla modalità osu!mania
                telegram.sendmessage("*osu!mania*\n" +
                                     "[Beatmap " + r['beatmap_id'] + "](" + 'https://osu.ppy.sh/b/' + r[
                                         'beatmap_id'] + ")\n*" + r['rank'] + "*\n" + mods +
                                     "\n*Punti*: " + r['score'] + "\n"
                                                                  "*Combo* x" + r['maxcombo'] + "\n"
                                                                                                "_Rainbow_ *300*: " +
                                     r['countgeki'] + "\n"
                                                      "*300*: " + r['count300'] + "\n"
                                                                                  "*100*: " + r[
                                         'count100'] + "\n"
                                                       "*200*: " + r['countkatu'] + "\n"
                                                                                    "*50*: " + r[
                                         'count50'] + "\n"
                                                      "*Miss*: " + r['countmiss'], sentin, source)
    else:
        # TODO: Mettere a posto sto schifo.
        if "osu" in royalgames[username.lower()]:
            r = osu.getuserrecent(royalgames[username.lower()]['osu'], 0)
            if "enabled_mods" in r:
                mods = osu.listmods(r['enabled_mods'])
            else:
                mods = ""
            telegram.sendmessage("*osu!*\n"
                                 "[Beatmap {0}](https://osu.ppy.sh/b/{0})\n"
                                 "*{1}*\n"
                                 "{2}\n"
                                 "*Punti*: {3}\n"
                                 "*Combo* x{4}\n"
                                 "*300*: {5}\n"
                                 "*100*: {6}\n"
                                 "*50*: {7}\n"
                                 "*Awesome*: {8}\n"
                                 "*Good*: {9}\n"
                                 "*Miss*: {10}"
                                 .format(r['beatmap_id'],
                                         r['rank'],
                                         mods,
                                         r['score'],
                                         r['maxcombo'],
                                         r['count300'],
                                         r['count100'],
                                         r['count50'],
                                         r['countgeki'],
                                         r['countkatu'],
                                         r['countmiss']), sentin, source)


def roll():
    print("@" + username + ": /roll")
    cmd = text.split(' ', 1)
    # Se è stato specificato un numero
    if len(cmd) >= 2:
        # Controlla che sia convertibile in un intero.
        try:
            m = int(cmd[1])
        except ValueError:
            telegram.sendmessage(chr(9888) + " Il numero specificato non è un intero.", sentin, source)
            return
    else:
        # Imposta il numero massimo a 100.
        m = 100
    # Prova a generare un numero casuale.
    if m == 34261891881215712181524122318242223183627453833:
        telegram.sendmessage("Numero casuale da 1 a _get rekt_:\n*@FrankRekt è scarso*", sentin, source)
    else:
        try:
            n = random.randrange(m) + 1
        except ValueError:
            telegram.sendmessage(chr(9888) + " Il numero specificato non è maggiore o uguale a 0.",
                                 sentin, source)
        # Se tutto va bene visualizza il numero generato
        else:
            telegram.sendmessage("Numero casuale da 1 a " + str(m) + ":\n*" + str(n) + "*", sentin,
                                 source)


def automah():
    print("@" + username + ": /automah")
    # Invia il messaggio.
    telegram.sendmessage("Automaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa! Devi funzionare, cavolo!",
                         sentin,
                         source)


def cv():
    print("@" + username + ": /cv")
    # Elenco di tutte le persone online su Discord
    tosend = "*Su Discord ora:*\n"
    r = discord.getwidgetdata("176353500710699008")
    musicstatus = str()
    for member in r['members']:
        m = dict()
        if 'bot' not in member or not member['bot']:
            # Credo di aver scritto il peggior algoritmo di sempre. gg me
            if 'channel_id' in member:
                if member['deaf'] or member['self_deaf']:
                    m['emoji'] = chr(128263)
                elif member['mute'] or member['self_mute']:
                    m['emoji'] = chr(128264)
                else:
                    m['emoji'] = chr(128266)
                m['channelname'] = discord.getchannelname(r, member['channel_id'])
            else:
                if member['status'] == "online":
                    if 'game' in member:
                        m['emoji'] = chr(128308)
                    else:
                        m['emoji'] = chr(128309)
                elif member['status'] == "idle":
                    m['emoji'] = chr(9899)
            if 'game' in member:
                m['gamename'] = member['game']['name']
            m['name'] = member['username']
            if 'gamename' in m and 'channelname' in m:
                tosend += "{emoji} *{channelname}* {name} | _{gamename}_\n".format(**m)
            elif 'gamename' in m:
                tosend += "{emoji} {name} | _{gamename}_\n".format(**m)
            elif 'channelname' in m:
                tosend += "{emoji} *{channelname}* {name}\n".format(**m)
            else:
                tosend += "{emoji} {name}\n".format(**m)
        # Controlla se l'utente è royal music
        elif member['id'] == "176358898851250176":
            if 'game' in member:
                musicstatus = "{emoji} *{channelname}* {songname}\n" \
                    .format(emoji="\U0001F3B5", channelname=discord.getchannelname(r, member['channel_id']),
                            songname=member['game']['name'])
    if musicstatus != "":
        tosend += musicstatus
    telegram.sendmessage(tosend, sentin, source)


def online():
    # Elenco di tutte le persone online su Steam
    print("@" + username + ": /online ")
    # Informa Telegram che il messaggio è stato ricevuto.
    telegram.sendchataction(sentin)
    cmd = text.split(" ")
    if len(cmd) >= 2:
        if cmd[1].lower() == "help":
            telegram.sendmessage(chr(128309) + " Online\n" +
                                 chr(128308) + " In gioco | Occupato\n" +
                                 chr(9899) + " Assente | Inattivo\n" +
                                 chr(128310) + " Disponibile per scambiare\n" +
                                 chr(128311) + " Disponibile per giocare", sentin, source)
    else:
        # Stringa utilizzata per ottenere informazioni su tutti gli utenti in una sola richiesta a steam
        userids = str()
        for membro in royalgames:
            if "steam" in royalgames[membro]:
                userids += str(royalgames[membro]["steam"]) + ','
        tosend = "*Su Steam ora:*\n"
        r = steam.getplayersummaries(userids)
        for player in r:
            # In gioco
            if 'gameextrainfo' in player:
                tosend += chr(128308) + " _" + player['gameextrainfo'] + "_ |"
            elif 'gameid' in player:
                tosend += chr(128308) + " _" + player['gameid'] + "_ |"
            # Online
            elif player['personastate'] == 1:
                tosend += chr(128309)
            # Occupato
            elif player['personastate'] == 2:
                tosend += chr(128308)
            # Assente o Inattivo
            elif player['personastate'] == 3 or player['personastate'] == 4:
                tosend += chr(9899)
            # Disponibile per scambiare
            elif player['personastate'] == 5:
                tosend += chr(128310)
            # Disponibile per giocare
            elif player['personastate'] == 6:
                tosend += chr(128311)
            if player['personastate'] != 0:
                tosend += " " + player['personaname'] + "\n"
        else:
            telegram.sendmessage(tosend, sentin, source)


def shrek():
    # Manda l'audio So much to do, so much to see
    print("@" + username + ": /shrekt ")
    telegram.senddocument("BQADBAADsQADiBjiAqYN-EBXASyhAg", sentin)


def diario():
    # Aggiungi una riga al diario Royal Games
    print("@" + username + ": /diario ")
    cmd = text.split(" ", 1)
    if len(cmd) > 1:
        if cmd[1].isprintable():
            cmd[1] = cmd[1].replace("\n", " ")
            fdiario = filemanager.readfile("diario.txt")
            fdiario += str(int(time.time())) + "|" + cmd[1] + "\n"
            filemanager.writefile("diario.txt", fdiario)
            telegram.sendmessage("Aggiunto al diario RYG.", sentin, source)
        else:
            telegram.sendmessage(chr(9888) + " Errore nella scrittura del messaggio.\n"
                                             "Visto che non ho la minima idea delle assurdita che ho scritto qui, "
                                             "potresti provare a togliere le emoji.", sentin, source)
    else:
        telegram.sendmessage(chr(9888) + " Non hai scritto niente sul diario!\n"
                                         "Sintassi corretta: /diario _quello che vuoi scrivere_",
                             sentin, source)


def leggi():
    # Leggi dal diario Royal Games
    print("@" + username + ": /leggi")
    telegram.sendmessage("[Apri il diario RYG](http://royal.steffo.me/diario.htm)!", sentin, source)


def balurage():
    print("@" + username + ": /balurage")
    # Rispondi commentando l'E3.
    telegram.sendmessage("MADDEN MADDEN MADDEN MADDEN MADDEN MADDEN MADDEN MADDEN MADDEN",
                         sentin, source)


def lolfree():
    global lolfreestring
    # Visualizza i campioni gratuiti di LoL di questa settimana
    print("@" + username + ": /lolfree")
    # Informa Telegram che il messaggio è stato ricevuto.
    telegram.sendchataction(sentin)
    ora = time.gmtime()
    cmd = text.split(" ", 1)
    if len(cmd) > 1:
        refresh = cmd[1].startswith("refresh")
    else:
        refresh = False
    # Controlla se i dati sono già stati scaricati.
    if lolfreestring is None or refresh:
        # Crea un nuovo set di dati.
        print("Aggiornamento champ gratuiti di League of Legends...")
        lolfreestring = "Champion gratuiti del `" + str(ora.tm_mday) + "/" + str(ora.tm_mon) + "/" + \
                        str(ora.tm_year) + " " + str(ora.tm_hour) + ":" + str(ora.tm_min) + "`\n"
        r = lol.getfreerotation()
        for champion in r:
            staticdata = lol.getchampionstaticdata(champion['id'])
            lolfreestring += "*" + staticdata['name'] + "* " + staticdata['title'] + '\n'
        print("Completato.")
    telegram.sendmessage(lolfreestring, sentin, source)


# Ciclo principale del bot
print("Bot avviato!")
while True:
    try:
        # Guarda il comando ricevuto.
        msg = telegram.getupdates()
        # Se il messaggio non è una notifica di servizio...
        if 'edit' in msg:
            if msg['edit']:
                if 'text' in msg['edit_data']:
                    # Salvatelo in una stringa
                    text = msg['edit_data']['text']
                    # Guarda l'ID della chat in cui è stato inviato
                    sentin = msg['edit_data']['chat']['id']
                    # ID del messaggio ricevuto
                    source = msg['edit_data']['message_id']
                    if 'username' in msg['edit_data']['from']:
                        # Salva l'username se esiste
                        username = msg['edit_data']['from']['username']
                    else:
                        # Altrimenti, salva l'userID
                        username = str(msg['edit_data']['from']['id'])
                    # Se sei un membro della Royal Games
                    if username.lower() in royalgames:
                        # Riconosci il comando.
                        if text.startswith('wow'):
                            wow()
        if 'text' in msg:
            # Salvatelo in una stringa
            text = msg['text']
            # Guarda l'ID della chat in cui è stato inviato
            sentin = msg['chat']['id']
            # ID del messaggio ricevuto
            source = msg['message_id']
            # Nome da visualizzare nella console per capire chi accidenti è che invia messaggi strani
            if 'username' in msg['from']:
                # Salva l'username se esiste
                username = msg['from']['username']
            else:
                # Altrimenti, salva l'userID
                username = str(msg['from']['id'])
            # Se sei un membro della Royal Games
            if username.lower() in royalgames:
                # Riconosci il comando.
                # Viene usato startswith perchè il comando potrebbe anche essere inviato in forma /ciao@RoyalBot.
                if text.startswith('/ahnonlosoio'):
                    ahnonlosoio()
                elif text.startswith('/ciaostefanino'):
                    ciaostefanino()
                elif text.startswith('/balurage') or text.startswith("/madden"):
                    balurage()
                elif text.startswith('/potatogift'):
                    potatogift()
                elif text.startswith('/ciaoruozi'):
                    ciaoruozi()
                elif text.startswith('/ehoh'):
                    ehoh()
                elif text.startswith('/playing'):
                    playing()
                elif text.startswith('/saldi'):
                    saldi()
                elif text.startswith('/sbam'):
                    sbam()
                elif text.startswith('/osu'):
                    osucmd()
                elif text.startswith('/roll'):
                    roll()
                elif text.startswith('/automah'):
                    automah()
                elif text.startswith('/cv'):
                    cv()
                elif text.startswith('/online'):
                    online()
                elif text.startswith('/shrek'):
                    shrek()
                elif text.startswith('/diario'):
                    diario()
                elif text.startswith('/leggi'):
                    leggi()
                elif text.startswith('/lolfree'):
                    lolfree()
                elif text.startswith('/crash'):
                    # Crasha il bot. Mi sembra geniale.
                    if username == 'Steffo':
                        raise Exception("Ho appena fatto crashare tutto apposta. Sono un genio.")
            else:
                print("@" + username + " bloccato.")
    except Exception as e:
        telegram.sendmessage(chr(9762) + " *ERRORE CRITICO:\n*"
                                         "{0}\n".format(repr(e)), -2141322)
        print("ERRORE CRITICO:\n"
              "{0}".format(repr(e)))
