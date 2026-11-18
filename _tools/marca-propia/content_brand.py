# -*- coding: utf-8 -*-
"""Sèrie «La nostra marca»: un producte heroi per post, to de venda directe.
Estructura: portada (claim + 3 arguments) · Què porta · Per què la nostra marca · El nostre consell."""

from content import BASE_TAGS, LEGAL_SUP, LEGAL_PS

BRAND_CLAIM = "Formulada per un laboratori farmacèutic en exclusiva per a farmàcies. Només la trobaràs aquí."
SIGN = "Marca Farmàcia del Diamant. Qualitat de laboratori, preu de marca pròpia. Demana-la al taulell."

BRAND_POSTS = [
 dict(id="B01", slug="marca-oli-dutxa", date="2026-11-26", time="19:00", code="FPBDO480S", kind="COS",
  name="Aceite de Ducha Protector", badge=["PELL MOLT", "SECA"],
  headline="L'oli de dutxa que recomanem quan la pell tiba",
  args=["Neteja sense arrossegar els lípids de la pell", "Calmant i nutritiu: alta tolerabilitat", "El consell: dutxa curta, tèbia, i crema en sortir"],
  porta=[("Oli de dutxa protector", "pensat per a pell molt seca i sensible"), ("Acció calmant i nutritiva", "deixa una pel·lícula protectora en lloc d'assecar"), ("Format de llarga durada", "amb dosificador, per a tota la família")],
  perque=[("Formulació farmacèutica", "d'un laboratori que només treballa per a farmàcies"), ("Alta tolerabilitat", "fet per a la pell que reacciona a tot"), ("Només aquí", "amb la nostra marca i el nostre consell")],
  consell=[("Aigua tèbia, 5 minuts", "l'aigua molt calenta és el primer enemic de la pell seca"), ("Eixuga sense fregar", "i hidrata en els 3 minuts següents"), ("Si pica o hi ha plaques", "que t'ho mirem o consulta el dermatòleg")],
  caption=("🚿 L'oli de dutxa que recomanem quan la pell tiba\n\n"
   "Cada hivern el mateix: la pell tiba, pica, s'escama. I sovint el problema és el gel de dutxa. Per això el nostre consell és canviar-lo per aquest, amb la nostra marca:\n\n"
   "✔ Neteja sense arrossegar els lípids de la pell.\n"
   "✔ Calmant i nutritiu, pensat per a pell molt seca i sensible: alta tolerabilitat.\n"
   "✔ Format de llarga durada amb dosificador.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: dutxa curta i tèbia, eixugar sense fregar i crema abans de 3 minuts. Si la picor no marxa o hi ha plaques, vine i t'ho mirem.\n\n" + SIGN),
  tags=["#pellseca", "#pellsensible", "#hivern", "#dermocosmetica", "#lanostramarca", "#consellfarmaceutic"]),

 dict(id="B02", slug="marca-melatonina-complex", date="2026-12-03", time="19:00", code="FPATMEZ2S", kind="SUP",
  name="Melatonina Complex", badge=["MELATONINA", "+ B6"],
  headline="Dormir-se abans. Amb el nostre consell, no a cegues.",
  args=["Melatonina, L-triptòfan i vitamina B6", "Sense gluten: 40 comprimits recoberts", "El consell: 30 minuts abans, sempre a la mateixa hora"],
  porta=[("Melatonina", "contribueix a reduir el temps necessari per adormir-se (1 mg abans d'anar al llit)"), ("L-triptòfan", "aminoàcid precursor de la serotonina i la melatonina"), ("Vitamina B6", "contribueix al funcionament normal del sistema nerviós")],
  perque=[("Fórmula completa", "no només melatonina: tres actius que treballen junts"), ("Sense gluten", "40 comprimits recoberts, fàcils d'empassar"), ("Amb consell", "et diem si és per a tu o no, abans de vendre'l")],
  consell=[("30 minuts abans d'anar al llit", "i cada dia a la mateixa hora"), ("Pantalles fora", "la melatonina no fa miracles amb el mòbil a la mà"), ("Si prens medicació", "o l'insomni dura setmanes: metge primer")],
  caption=("🌙 Dormir-se abans. Amb el nostre consell, no a cegues.\n\n"
   "Hi ha melatonines a tot arreu. La nostra la recomanem per tres raons:\n\n"
   "✔ Fórmula completa: melatonina, L-triptòfan i vitamina B6.\n"
   "✔ Sense gluten, 40 comprimits recoberts.\n"
   "✔ La melatonina contribueix a reduir el temps necessari per adormir-se (prenent 1 mg poc abans d'anar al llit), i la B6 al funcionament normal del sistema nerviós.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: 30 minuts abans d'anar al llit, cada dia a la mateixa hora, i pantalles fora. Si prens altres medicaments o l'insomni dura setmanes, primer el metge.\n\n" + SIGN + "\n\n" + LEGAL_SUP),
  tags=["#melatonina", "#dormir", "#insomni", "#descans", "#lanostramarca", "#consellfarmaceutic"]),

 dict(id="B03", slug="marca-vitamina-c-20", date="2026-12-10", time="19:00", code="FPCAVC20S", kind="COS",
  name="Sèrum Vitamina C 20%", badge=["VITAMINA C", "20%"],
  headline="Vitamina C al 20%. Pura. Nostra.",
  args=["Concentració declarada: 20%", "Actiu pur, sense fórmules diluïdes", "El consell: al matí, i protecció solar a sobre"],
  porta=[("Vitamina C al 20%", "la concentració s'indica a l'envàs, no cal creure-ho de paraula"), ("Actiu pur d'ús extern", "pensat per a lluminositat i to uniforme"), ("Flascó amb comptagotes", "poques gotes per aplicació: dura")],
  perque=[("Concentració real", "un sèrum d'actiu pur, no una crema amb «una mica» de vitamina C"), ("Preu de marca pròpia", "qualitat de laboratori sense pagar la publicitat"), ("Consell inclòs", "t'expliquem com introduir-lo segons la teva pell")],
  consell=[("Al matí, sobre la pell neta", "4-5 gotes, i després la crema i la protecció solar"), ("Pell sensible?", "comença dia sí, dia no"), ("Guarda'l tancat i sense llum", "la vitamina C s'oxida amb l'aire i el sol")],
  caption=("🍊 Vitamina C al 20%. Pura. Nostra.\n\n"
   "Molts sèrums «amb vitamina C» en porten una quantitat simbòlica. El nostre indica la concentració a l'envàs: 20%.\n\n"
   "✔ Actiu pur, d'ús extern, per a lluminositat i to uniforme.\n"
   "✔ Flascó amb comptagotes: 4-5 gotes per aplicació.\n"
   "✔ Qualitat de laboratori, preu de marca pròpia.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: al matí sobre la pell neta, després crema i protecció solar. Si tens la pell sensible, comença dia sí, dia no. Guarda'l tancat i lluny de la llum.\n\n" + SIGN),
  tags=["#vitaminac", "#serum", "#lluminositat", "#rutinafacial", "#lanostramarca", "#dermocosmetica"]),

 dict(id="B04", slug="marca-collagen-age", date="2026-12-17", time="19:00", code="FPAACL12S", kind="SUP",
  name="Collagen Age Formula", badge=["VERISOL®", "+ HYABEST®"],
  headline="Col·lagen amb nom i cognoms: Verisol® i Hyabest®",
  args=["Pèptids de col·lagen Verisol® i àcid hialurònic Hyabest®", "Sense gluten ni sucres: 20 flascons bevibles", "El consell: un flascó al dia, mínim 2 mesos"],
  porta=[("Col·lagen Verisol®", "pèptids de col·lagen bioactius, amb marca registrada i estudis propis"), ("Àcid hialurònic Hyabest®", "d'alta puresa"), ("Manganès", "contribueix a la formació normal del teixit connectiu")],
  perque=[("Ingredients amb marca", "no «col·lagen» genèric: Verisol® i Hyabest®"), ("Sense gluten ni sucres", "flascó bevible, còmode cada dia"), ("Consell honest", "et diem què pots esperar-ne i què no")],
  consell=[("Un flascó al dia", "millor sempre a la mateixa hora"), ("Constància: 2-3 mesos", "els complements no funcionen a ratxes"), ("Dolor articular persistent?", "primer el metge, després el complement")],
  caption=("💪 Col·lagen amb nom i cognoms: Verisol® i Hyabest®\n\n"
   "«Col·lagen» ho posa tothom. El que importa és quin. El nostre porta:\n\n"
   "✔ Pèptids de col·lagen Verisol®, amb marca registrada i estudis propis.\n"
   "✔ Àcid hialurònic Hyabest® d'alta puresa.\n"
   "✔ Manganès, que contribueix a la formació normal del teixit connectiu.\n"
   "✔ Sense gluten ni sucres. 20 flascons bevibles.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: un flascó al dia durant 2-3 mesos; els complements no funcionen a ratxes. Si tens dolor articular persistent, primer el metge.\n\n" + SIGN + "\n\n" + LEGAL_SUP),
  tags=["#collagen", "#verisol", "#acidhialuronic", "#articulacions", "#lanostramarca", "#complementsalimentaris"]),

 dict(id="B05", slug="marca-floratab", date="2027-01-07", time="19:00", code="FPATFTZ3S", kind="SUP",
  name="Floratab", badge=["SACCHAROMYCES", "BOULARDII"],
  headline="Soca identificada. No «probiòtics» a l'engròs.",
  args=["Saccharomyces boulardii CNCM I-3799", "Sense sucre ni lactosa: 24 càpsules", "El consell: durant i després de l'antibiòtic"],
  porta=[("Saccharomyces boulardii", "llevat, no bacteri: no l'afecten els antibiòtics"), ("Soca CNCM I-3799", "identificada i dipositada: saps exactament què prens"), ("Sense sucre ni lactosa", "24 càpsules")],
  perque=[("Soca amb nom", "la diferència entre un ferment i «un probiòtic qualsevol»"), ("Es pot prendre amb l'antibiòtic", "perquè és un llevat"), ("Consell al taulell", "quan, quant i fins quan")],
  consell=[("Amb l'antibiòtic, des del primer dia", "i continua una setmana després d'acabar-lo"), ("Viatges i canvis de dieta", "porta'l a la maleta"), ("Diarrea amb febre o sang", "metge, no complement")],
  caption=("🦠 Un ferment amb soca identificada. No «probiòtics» a l'engròs.\n\n"
   "Quan ens demaneu un probiòtic per a l'antibiòtic, aquest és el que recomanem:\n\n"
   "✔ Saccharomyces boulardii CNCM I-3799: soca identificada i dipositada.\n"
   "✔ És un llevat, no un bacteri: es pot prendre alhora que l'antibiòtic.\n"
   "✔ Sense sucre ni lactosa, 24 càpsules.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: des del primer dia d'antibiòtic i fins una setmana després d'acabar-lo. Si la diarrea va amb febre o sang, o dura més de dos dies, metge.\n\n" + SIGN + "\n\n" + LEGAL_SUP),
  tags=["#probiotics", "#antibiotics", "#florintestinal", "#digestio", "#lanostramarca", "#consellfarmaceutic"]),

 dict(id="B06", slug="marca-magnesium-cap", date="2027-01-14", time="19:00", code="FPATMGZ0S", kind="SUP",
  name="Magnesium Cap", badge=["MAGNESI", "SUCROSOMIAL"],
  headline="El magnesi per a qui no tolera el magnesi",
  args=["Magnesi en forma sucrosomial", "Sense gluten: 30 càpsules, una al dia", "El consell: amb l'esmorzar, un mes sencer"],
  porta=[("Magnesi sucrosomial", "el mineral va encapsulat en una matriu de fosfolípids i sucroèsters"), ("Pensat per a la tolerància digestiva", "la queixa més habitual amb altres formes de magnesi"), ("Contribueix a disminuir el cansament i la fatiga", "i al funcionament normal dels músculs")],
  perque=[("Forma, no només dosi", "no tots els magnesis s'absorbeixen ni es toleren igual"), ("Una càpsula al dia", "30 càpsules, sense gluten"), ("Consell personalitzat", "si prens altres suplements o medicació, t'ho ordenem")],
  consell=[("Una càpsula amb l'esmorzar", "o al vespre si el prefereixes per relaxar-te"), ("Un mes sencer", "abans de decidir si et va bé"), ("Ronyó delicat o medicació crònica?", "pregunta'ns abans")],
  caption=("⚡ Magnesi sucrosomial: el que recomanem a qui no tolera els altres\n\n"
   "«El magnesi em desfà l'estómac.» Ho sentim cada setmana. Per això la nostra marca porta magnesi sucrosomial:\n\n"
   "✔ El mineral va encapsulat en una matriu de fosfolípids i sucroèsters, pensada per a la tolerància digestiva.\n"
   "✔ El magnesi contribueix a disminuir el cansament i la fatiga i al funcionament normal dels músculs.\n"
   "✔ Una càpsula al dia, 30 càpsules, sense gluten.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: una càpsula amb l'esmorzar durant un mes sencer abans de decidir. Si tens el ronyó delicat o prens medicació crònica, pregunta'ns abans.\n\n" + SIGN + "\n\n" + LEGAL_SUP),
  tags=["#magnesi", "#cansament", "#energia", "#rampes", "#lanostramarca", "#complementsalimentaris"]),

 dict(id="B07", slug="marca-talons-urea", date="2027-01-21", time="19:00", code="FPCCCT51S", kind="COS",
  name="Crema Talones Urea 10%", badge=["UREA", "10%"],
  headline="Urea al 10%. Sense perfum. Talons cuidats.",
  args=["Urea al 10% + ceramides", "Sense perfum: alta tolerabilitat", "El consell: cada nit, amb mitjons de cotó"],
  porta=[("Urea al 10%", "estova la pell engruixida i reté la hidratació"), ("Ceramides", "reparen la barrera de la pell del taló"), ("Sense perfum", "acció reparadora intensiva, també per a pells reactives")],
  perque=[("Concentració declarada", "10% d'urea: ni massa poc per no fer res, ni tant que irriti"), ("Sense perfum", "alta tolerabilitat"), ("Només aquí", "amb la nostra marca i el nostre consell")],
  consell=[("Cada nit, capa generosa", "i mitjons de cotó per dormir"), ("Primer la pedra tosca, un cop per setmana", "amb el peu sec, mai en carn viva"), ("Diabetis?", "abans de res, que t'ho mirem")],
  caption=("🦶 Urea al 10% i sense perfum: la crema de talons que recomanem\n\n"
   "Hi ha moltes cremes de talons. Aquesta és la nostra, i la recomanem per tres raons:\n\n"
   "✔ Urea al 10%: estova la pell engruixida i reté la hidratació. Ceramides que reparen la barrera cutània.\n"
   "✔ Sense perfum: alta tolerabilitat, també per a pells reactives.\n"
   "✔ Concentració declarada a l'envàs.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: una capa generosa cada nit amb mitjons de cotó, i pedra tosca un cop per setmana amb el peu sec. Si tens diabetis, abans de res, que t'ho mirem.\n\n" + SIGN),
  tags=["#talons", "#urea", "#peus", "#pellseca", "#lanostramarca", "#dermocosmetica"]),

 dict(id="B08", slug="marca-gel-hyaluronic", date="2027-01-28", time="19:00", code="FPCVGI30S", kind="COS",
  name="Gel Hyaluronic 40%", badge=["ÀCID", "HIALURÒNIC"],
  headline="Àcid hialurònic en gel. Hidratació sense greix.",
  args=["Àcid hialurònic + vitamina E", "Textura gel: s'absorbeix de seguida, sense greix", "El consell: sobre la pell humida, matí i nit"],
  porta=[("Àcid hialurònic", "reté aigua a la pell: hidratació intensiva"), ("Vitamina E", "antioxidant que protegeix la fórmula i la pell"), ("Textura gel", "per a totes les pells, també grasses o mixtes")],
  perque=[("Un sol producte per a tothom", "a casa el poden fer servir tots"), ("Alta tolerabilitat", "textura lleugera, sense sensació de greix"), ("Preu de marca pròpia", "per fer-lo servir cada dia, no només a les ocasions")],
  consell=[("Sobre la pell una mica humida", "l'àcid hialurònic necessita aigua per treballar"), ("Matí i nit, abans de la crema", "o sol, si tens la pell grassa"), ("Pell molt seca?", "combina'l amb la Crema Hidratante Antiedad")],
  caption=("💧 Hidratació intensiva en gel: àcid hialurònic i vitamina E\n\n"
   "El producte que més recomanem quan algú ens diu «tinc la pell deshidratada però no vull cremes greixoses»:\n\n"
   "✔ Àcid hialurònic, que reté aigua a la pell.\n"
   "✔ Vitamina E antioxidant.\n"
   "✔ Textura gel, lleugera: alta tolerabilitat, també per a pells grasses o mixtes.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: aplica'l sobre la pell una mica humida, matí i nit, abans de la crema. Si tens la pell molt seca, combina'l amb la nostra Crema Hidratante Antiedad.\n\n" + SIGN),
  tags=["#acidhialuronic", "#hidratacio", "#rutinafacial", "#pelldeshidratada", "#lanostramarca", "#dermocosmetica"]),

 dict(id="B09", slug="marca-clorhexidina", date="2027-02-04", time="19:00", code="FPCCLX61S", kind="COS",
  name="Colutorio Clorhexidina 0,2%", badge=["CLORHEXIDINA", "0,2%"],
  headline="Clorhexidina 0,2%. Sense alcohol. Menys taques.",
  args=["Clorhexidina 0,2% amb tecnologia Clorex-A2G®", "Sense alcohol: no cou", "El consell: ús puntual, quan el dentista t'ho indiqui"],
  porta=[("Clorhexidina 0,2%", "acció antitàrtar i purificant"), ("Clorex-A2G®", "patent que redueix al mínim el risc de pigmentació de les dents"), ("Sense alcohol", "200 ml, no cou ni asseca la boca")],
  perque=[("Resol la queixa clàssica", "la clorhexidina taca; aquesta, molt menys"), ("Sense alcohol", "alta tolerabilitat en genives sensibles"), ("Consell d'ús", "et diem quants dies i com, perquè no és per a cada dia")],
  consell=[("Ús puntual", "després d'una intervenció o quan el dentista t'ho indiqui"), ("No més de 2 setmanes seguides", "sense consell professional"), ("Espera 30 minuts després del raspallat", "la pasta de dents en redueix l'efecte")],
  caption=("🦷 Clorhexidina 0,2% sense alcohol i amb menys taques\n\n"
   "La clorhexidina és la referència quan el dentista en demana, però té dues pegues: cou i taca. El nostre col·lutori respon a totes dues:\n\n"
   "✔ Clorhexidina al 0,2% amb tecnologia Clorex-A2G®, que redueix al mínim el risc de pigmentació.\n"
   "✔ Sense alcohol: alta tolerabilitat en genives sensibles.\n"
   "✔ Flascó de 200 ml.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: ús puntual, mai més de dues setmanes seguides sense consell professional, i espera 30 minuts després del raspallat. Pregunta'ns i t'ho expliquem.\n\n" + SIGN),
  tags=["#clorhexidina", "#salutbucal", "#genives", "#dentista", "#lanostramarca", "#consellfarmaceutic"]),

 dict(id="B10", slug="marca-niacinamida", date="2027-02-11", time="19:00", code="FPANIA10S", kind="COS",
  name="Sèrum Niacinamida 10%", badge=["NIACINAMIDA", "10%"],
  headline="Niacinamida al 10%. Va bé a gairebé tothom.",
  args=["Concentració declarada: 10%", "Alta tolerabilitat: pell grassa, mixta o sensible", "El consell: matí o nit, i combina amb tot"],
  porta=[("Niacinamida al 10%", "vitamina B3 d'ús extern"), ("Per a porus visibles, greix i to irregular", "l'actiu més versàtil de la rutina"), ("Flascó amb comptagotes", "poques gotes per aplicació")],
  perque=[("Concentració real", "10%, la que fa feina sense irritar"), ("Alta tolerabilitat", "la recomanem fins i tot a qui no tolera els àcids"), ("Preu de marca pròpia", "actiu pur sense pagar l'embolcall")],
  consell=[("Matí o nit, sobre la pell neta", "3-4 gotes abans de la crema"), ("Combina amb hialurònic i retinol", "és el company fàcil de la rutina"), ("Si et pica", "redueix a dia sí, dia no, i pregunta'ns")],
  caption=("✨ Niacinamida al 10%: l'actiu que va bé a gairebé tothom\n\n"
   "Si només haguéssim de recomanar un sèrum, seria aquest:\n\n"
   "✔ Niacinamida (vitamina B3) al 10%, concentració declarada a l'envàs.\n"
   "✔ Per a porus visibles, excés de greix i to irregular.\n"
   "✔ Alta tolerabilitat: pell grassa, mixta o sensible.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: 3-4 gotes matí o nit sobre la pell neta, abans de la crema. Combina bé amb l'àcid hialurònic i amb el retinol. Si et pica, passa a dia sí, dia no.\n\n" + SIGN),
  tags=["#niacinamida", "#serum", "#porus", "#pellgrassa", "#lanostramarca", "#dermocosmetica"]),

 dict(id="B11", slug="marca-retinol", date="2027-02-18", time="19:00", code="FPCAVA21S", kind="COS",
  name="Sérum Noche Retinol 0,3% Puro", badge=["RETINOL PUR", "0,3%"],
  headline="Retinol pur al 0,3%. Potent, però amb consell.",
  args=["Retinol pur al 0,3%, concentració declarada", "Retexturitzant global i antiarrugues", "El consell: de nit, començant dues nits per setmana"],
  porta=[("Retinol pur al 0,3%", "no un derivat: retinol, a la concentració que indica l'envàs"), ("Retexturitzant global", "per a textura, arrugues i to"), ("Envàs airless", "protegeix l'actiu de l'aire i la llum")],
  perque=[("Dosi seriosa", "0,3% és concentració d'ús real, no de reclam"), ("Amb consell", "el retinol mal introduït irrita; nosaltres t'acompanyem"), ("Només aquí", "amb la nostra marca")],
  consell=[("Només de nit", "dues nits per setmana les 3 primeres setmanes, després cada 2 nits"), ("Protecció solar de dia, sempre", "i hidratant generosa"), ("No en embaràs ni lactància", "ni la mateixa nit que els àcids")],
  caption=("🌙 Retinol pur al 0,3%. Potent, però amb consell.\n\n"
   "El retinol és l'actiu antiedat amb més evidència, i també el que més gent abandona per fer-lo servir malament. El nostre:\n\n"
   "✔ Retinol pur al 0,3%, concentració declarada a l'envàs. Retexturitzant global i antiarrugues.\n"
   "✔ Envàs airless que protegeix l'actiu.\n"
   "✔ I el més important: te l'expliquem abans que te l'emportis.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: només de nit, dues nits per setmana les tres primeres setmanes i després cada dues nits; protecció solar de dia sempre. No durant l'embaràs ni la lactància, ni la mateixa nit que els àcids.\n\n" + SIGN),
  tags=["#retinol", "#antiedat", "#serum", "#rutinanocturna", "#lanostramarca", "#dermocosmetica"]),

 dict(id="B12", slug="marca-gel-intim", date="2027-02-25", time="19:00", code="FPICDI61S", kind="COS",
  name="Gel Íntimo Fisiológico pH 5,5", badge=["pH", "5,5"],
  headline="pH 5,5. Higiene íntima que respecta la flora.",
  args=["pH fisiològic 5,5", "Liquen i calèndula: alta tolerabilitat", "El consell: només ús extern, un cop al dia"],
  porta=[("pH 5,5", "el de la zona íntima en edat fèrtil: respecta la flora"), ("Liquen d'Islàndia", "suavitzant"), ("Calèndula", "calmant, per a l'ús diari")],
  perque=[("Respecta la flora", "un gel de dutxa normal té un pH que no toca"), ("Alta tolerabilitat", "fórmula suau per a cada dia"), ("Tres pH a la gamma", "5,5 diari, 6,5 calmant, 4,5 actiu: t'ajudem a triar")],
  consell=[("Només ús extern", "mai dutxes internes"), ("Un cop al dia n'hi ha prou", "més no és millor"), ("Picor, olor o fluix diferent?", "metge o ginecòleg abans de canviar de gel")],
  caption=("🌸 pH 5,5, liquen i calèndula: higiene íntima sense agredir\n\n"
   "El gel de dutxa de cada dia té un pH que no és el de la zona íntima. Per això recomanem un gel específic, i aquest és el nostre:\n\n"
   "✔ pH fisiològic 5,5, que respecta la flora.\n"
   "✔ Liquen d'Islàndia i calèndula: alta tolerabilitat per a l'ús diari.\n"
   "✔ Forma part d'una gamma amb tres pH (5,5 diari, 6,5 calmant, 4,5 actiu) i t'ajudem a triar.\n\n"
   f"{BRAND_CLAIM}\n\n"
   "El consell: només ús extern, un cop al dia. Si hi ha picor, olor o fluix diferent de l'habitual, primer el metge o el ginecòleg.\n\n" + SIGN),
  tags=["#higieneintima", "#salutfemenina", "#ph", "#dona", "#lanostramarca", "#consellfarmaceutic"]),
]
