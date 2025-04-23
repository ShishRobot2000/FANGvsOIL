# 📊 Tech vs Oil – Analisi e Previsione di Mercato (2014–2024)

Questo progetto Python confronta le performance delle principali aziende tecnologiche americane (FANG++, quindi Facebook/META, Amazon, Netflix, Google/Alphabet, Apple, Microsoft e Tesla) con quelle delle più grandi compagnie petrolifere mondiali (ExxonMobil, Chevron, Shell, BP e TotalEnergies). L'obiettivo è osservare e analizzare l'andamento storico di ciascun titolo azionario su un periodo di dieci anni, calcolare il rendimento cumulativo, stimare la media di crescita per ciascun settore e infine provare a proiettare l’andamento futuro dei due settori nei prossimi cinque anni usando un modello di regressione lineare.

Il programma inizia scaricando i dati storici dal 1° gennaio 2014 al 1° gennaio 2024 utilizzando la libreria `yfinance`, che permette di ottenere i prezzi azionari da Yahoo Finance. Per ciascun titolo, viene selezionata la colonna “Adjusted Close” e da essa vengono calcolati i rendimenti giornalieri percentuali, che successivamente vengono cumulati nel tempo per mostrare quanto sarebbe cresciuto 1 dollaro investito all'inizio del periodo.

Successivamente, vengono calcolate due serie di medie: la media dei titoli tecnologici (Tech) e la media dei titoli petroliferi (Oil). Queste curve rappresentano l’andamento aggregato dei due settori e permettono un confronto più semplice e pulito rispetto alle singole azioni. Le due medie settoriali vengono poi utilizzate come base per una previsione futura. Questa previsione si basa su una regressione lineare semplice, implementata con la libreria `scikit-learn`, che viene addestrata sui dati storici e proiettata nei cinque anni successivi (circa 1260 giorni lavorativi).

Il risultato del programma è un grafico suddiviso in due sezioni. Nella prima sezione vengono mostrate tutte le azioni singole, sia tech che oil, con le medie di settore evidenziate. Le aziende tech sono rappresentate con linee continue, quelle oil con linee tratteggiate. Nella seconda sezione del grafico si vedono solo le medie settoriali, accompagnate dalle proiezioni future tratteggiate: una per la media tech e una per quella oil. In questo modo si ottiene una visualizzazione chiara di passato e futuro, con l’andamento stimato dai modelli matematici.

Per eseguire correttamente questo script sono necessarie alcune librerie Python: `yfinance` per il download dei dati, `pandas` per la manipolazione dei dati, `numpy` per i calcoli numerici, `matplotlib` per la generazione dei grafici, e `scikit-learn` per la regressione lineare. Queste librerie possono essere installate tramite `pip` con il seguente comando:

pip install yfinance pandas matplotlib scikit-learn

Una volta installato tutto, basta eseguire lo script con:

python fang_vs_oil_forecast.py

I dati utilizzati provengono esclusivamente da Yahoo Finance e vengono aggiornati ogni volta che si esegue il programma. I ticker analizzati per il settore tech sono: META, AMZN, NFLX, GOOGL, AAPL, MSFT e TSLA. Per il settore oil invece: XOM, CVX, SHEL, BP e TTE.

Lo scopo di questo progetto è puramente educativo: serve ad esplorare come utilizzare dati reali dei mercati finanziari per fare analisi comparativa, costruire indicatori settoriali e creare modelli predittivi semplici. Le previsioni effettuate non costituiscono in alcun modo una raccomandazione finanziaria. Sono piuttosto un esercizio per comprendere l’applicazione di strumenti matematici e statistici nel mondo della finanza quantitativa.

Questo progetto può essere ampliato in futuro con nuove funzionalità, come il calcolo del rischio (volatilità, drawdown, Sharpe Ratio), l’uso di modelli predittivi più avanzati come XGBoost o LSTM, oppure la trasformazione dell’intero sistema in una web app interattiva con Streamlit. Un'altra estensione interessante sarebbe collegare il sistema a un’analisi del sentiment proveniente dalle notizie o dai social, così da arricchire la previsione con segnali esogeni.

Creato da Pietro Pellegrino – Aprile 2025. Tutti i diritti riservati. Distribuito con licenza MIT.
