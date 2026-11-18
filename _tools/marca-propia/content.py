# -*- coding: utf-8 -*-
"""Contingut dels posts de marca pròpia (català). SUP = complement alimentari, PS = producte sanitari, COS = cosmètic."""

BASE_TAGS = ["#farmaciadeldiamant", "#gracia", "#barcelona", "#farmacia", "#marcapropia", "#farmaciadebarri", "#salut"]
LEGAL_SUP = "Complement alimentari: no substitueix una dieta variada i equilibrada ni un estil de vida saludable."
LEGAL_PS = "Producte sanitari. Llegiu detingudament les instruccions d'ús."
CTA = "Vine i te'ls expliquem al taulell: cada persona és diferent."

POSTS = [
 dict(id="P01", slug="mp-defenses", date="2026-11-21", time="12:00",
  title="Defenses a punt per a l'hivern",
  hook="La nostra gamma de marca pròpia per a aquesta època de l'any.",
  products=[
   dict(code="FPAAIF63S", name="Immuno Fluid", kind="SUP", body="Xarop amb equinàcia (Echinoshield®), fructooligosacàrids, zinc, seleni i vitamines B6 i B12. Flascó de 200 ml."),
   dict(code="FPALCRZ2S", name="Immuno Complex", kind="SUP", body="Comprimits amb quercetina, lactoferrina, vitamina C, vitamina B3 i zinc. 30 comprimits."),
   dict(code="FPAVCEG2S", name="Vit C 1000", kind="SUP", body="Vitamina C en comprimits efervescents. 20 comprimits per dissoldre en aigua."),
   dict(code="FPAVD3Z0S", name="Vitamina D3", kind="SUP", body="Vitamina D3 en comprimits masticables, còmodes per prendre cada dia. 60 comprimits."),
  ],
  caption=("❄️ Defenses a punt per a l'hivern\n\n"
   "Cada novembre arriba la mateixa pregunta al taulell: «què puc prendre per a les defenses?». Aquesta és la nostra gamma de marca pròpia.\n\n"
   "• Immuno Fluid: xarop amb equinàcia, zinc, seleni i vitamines B6 i B12.\n"
   "• Immuno Complex: quercetina, lactoferrina, vitamina C, B3 i zinc.\n"
   "• Vit C 1000: efervescent, fàcil de prendre.\n"
   "• Vitamina D3: masticable, per als mesos amb poc sol.\n\n"
   "La vitamina C, la vitamina D i el zinc contribueixen al funcionament normal del sistema immunitari. Cap complement, però, substitueix dormir bé, menjar variat i moure's.\n\n"
   f"Si prens medicació o tens dubtes, pregunta'ns: no tots serveixen per a tothom. {CTA}\n\n{LEGAL_SUP}"),
  tags=["#defenses", "#vitaminac", "#vitaminad", "#zinc", "#hivern", "#complementsalimentaris"]),

 dict(id="P02", slug="mp-gola", date="2026-11-24", time="19:00",
  title="Gola irritada? Això és el que tenim",
  hook="Quatre opcions de marca pròpia per a la picor i la coïssor de gola.",
  products=[
   dict(code="FPAAGPZ2S", name="Golaplus", kind="SUP", body="Càpsules masticables amb Larixicina®, equinàcia, perilla, pròpolis, erísim, regalèssia i olis essencials. 20 càpsules."),
   dict(code="FPAAPRZ3S", name="Pastillas Oralflu Garganta", kind="PS", body="Comprimits per xuclar amb gust de menta, sense gluten ni lactosa. Calmen la irritació i alleugen la picor. 20 comprimits."),
   dict(code="FPAASG11S", name="Spray Oralflu Garganta", kind="PS", body="Esprai bucal amb gust de menta que calma les irritacions de la cavitat oral. Flascó de 20 ml."),
   dict(code="FPPSGJZ0S", name="Golatab Junior", kind="SUP", body="Pastilles per xuclar amb mel de Manuka, malva, plantatge i vitamina C. Gust de gerds, a partir de 6 anys. 20 pastilles."),
  ],
  caption=("🗣️ Gola irritada? Això és el que tenim\n\n"
   "Picor, coïssor, veu rasposa… la gola és la consulta estrella d'aquestes setmanes. De marca pròpia tenim:\n\n"
   "• Golaplus: càpsules masticables amb pròpolis, equinàcia i erísim.\n"
   "• Pastillas Oralflu Garganta: comprimits de menta que calmen la irritació.\n"
   "• Spray Oralflu Garganta: esprai per a les irritacions de la boca i la gola.\n"
   "• Golatab Junior: pastilles amb mel de Manuka i malva, a partir de 6 anys.\n\n"
   "Beure sovint, no forçar la veu i humitejar l'ambient ajuda tant com qualsevol producte. Si hi ha febre alta, dificultat per empassar o dura més d'una setmana, toca visita al metge.\n\n"
   f"{CTA}\n\n{LEGAL_PS} {LEGAL_SUP}"),
  tags=["#malDeGola", "#gola", "#hivern", "#refredat", "#propolis", "#consellfarmaceutic"]),

 dict(id="P03", slug="mp-tos", date="2026-11-28", time="12:00",
  title="Tos: xarops i esprai de marca pròpia",
  hook="Per a adults, per a infants i per al nas tapat.",
  products=[
   dict(code="FPAAST63S", name="Jarabe Tuss Control sin azúcar", kind="PS", body="Xarop sense sucre amb gust de fruits vermells. Contraresta la tos, el mal de gola i el malestar. Flascó de 150 ml."),
   dict(code="FPAASJ63S", name="Jarabe Tuss Control Pediatric", kind="PS", body="Xarop amb gust de maduixa, a partir d'1 any. Calma la tos seca i productiva i protegeix la mucosa. Flascó de 150 ml."),
   dict(code="FPAASP62S", name="Jarabe Propóleo & Drosera", kind="SUP", body="Xarop amb Larixicina®, grindèlia, liquen, dròsera, pròpolis, eucaliptus, farigola i mel. Flascó de 150 ml."),
   dict(code="FPAMFS20S", name="Spray Mucoflu", kind="PS", body="Esprai nasal que descongestiona el nas i afavoreix la respiració. Flascó de 30 ml."),
  ],
  caption=("🤧 Tos: xarops i esprai de marca pròpia\n\n"
   "La tos és un mecanisme de defensa, però quan no deixa dormir cal fer-hi alguna cosa. Les nostres opcions:\n\n"
   "• Jarabe Tuss Control sense sucre: per a adults, gust de fruits vermells.\n"
   "• Jarabe Tuss Control Pediatric: a partir d'1 any, gust de maduixa.\n"
   "• Jarabe Propóleo & Drosera: amb pròpolis, farigola, eucaliptus i mel.\n"
   "• Spray Mucoflu: per al nas tapat.\n\n"
   "Consulta el metge si la tos dura més de tres setmanes, si hi ha febre persistent, dificultat per respirar o dolor al pit. En infants petits, sempre amb consell del pediatre o nostre.\n\n"
   f"{CTA}\n\n{LEGAL_PS} {LEGAL_SUP}"),
  tags=["#tos", "#xarop", "#refredat", "#hivern", "#nens", "#consellfarmaceutic"]),

 dict(id="P04", slug="mp-refredat", date="2026-12-01", time="19:00",
  title="El kit de refredat",
  hook="Vitamina C, NAC i aigua de mar: els bàsics de desembre.",
  products=[
   dict(code="FPAAF5Z1S", name="Flu C 500", kind="SUP", body="Comprimits efervescents amb vitamina C, saüc, N-acetilcisteïna, pròpolis i zinc. 20 comprimits."),
   dict(code="FPAMUCX0S", name="NAC600 Complex", kind="SUP", body="Sobres amb Larixicina®, N-acetilcisteïna, bromelina, farigola, vitamina C, altea, heura i zinc. 10 sobres."),
   dict(code="FPCNIP50S", name="Spray Nasal Hipertónico", kind="PS", body="Solució salina hipertònica amb àcid hialurònic, sense conservants. Per a adults i infants. Flascó de 100 ml."),
   dict(code="FPAAMFX2S", name="NAC300 Complex", kind="SUP", body="Sobres amb N-acetilcisteïna, vitamina C, zinc i extractes d'eucaliptus, farigola, heura i altea. 12 sobres."),
  ],
  caption=("🧣 El kit de refredat\n\n"
   "Un refredat dura el que dura (entre 7 i 10 dies), però es pot passar millor. El nostre kit de marca pròpia:\n\n"
   "• Flu C 500: vitamina C, saüc, NAC, pròpolis i zinc en efervescent.\n"
   "• NAC600 Complex i NAC300 Complex: sobres amb N-acetilcisteïna i extractes de plantes.\n"
   "• Spray Nasal Hipertónico: aigua de mar amb àcid hialurònic per netejar el nas, també per als petits.\n\n"
   "Recorda: els antibiòtics no serveixen per als refredats. Si tens febre alta més de tres dies o et costa respirar, visita el metge.\n\n"
   f"{CTA}\n\n{LEGAL_PS} {LEGAL_SUP}"),
  tags=["#refredat", "#vitaminac", "#nasTapat", "#hivern", "#grip", "#consellfarmaceutic"]),

 dict(id="P05", slug="mp-mans-llavis", date="2026-12-05", time="12:00",
  title="Mans i llavis protegits del fred",
  hook="Els petits bàsics de butxaca per a l'hivern.",
  products=[
   dict(code="FPCCCM40S", name="Crema Nutritiva de Manos", kind="COS", body="Crema de mans amb mel, que nodreix i protegeix. Textura que s'absorbeix de pressa per poder-la fer servir sovint."),
   dict(code="FPCCMA40S", name="Crema Antiedad Manos y Uñas", kind="COS", body="Crema per a mans i ungles amb àcid hialurònic. Per a la pell de les mans que comença a mostrar el pas del temps."),
   dict(code="FPCACL11S", name="Reparador Labios", kind="COS", body="Reparador de llavis amb pròpolis, arbre del te, àloe vera i vitamina E. Per a llavis secs i esquerdats."),
   dict(code="FPCASL11S", name="Protector Labios", kind="COS", body="Bàlsam protector amb mantega de karité i vitamines A i E. El que has de portar sempre a la butxaca."),
  ],
  caption=("🧤 Mans i llavis protegits del fred\n\n"
   "Fred, vent, calefacció i rentar-se les mans sovint: la combinació perfecta perquè la pell s'esquerdi. Els nostres bàsics de marca pròpia:\n\n"
   "• Crema Nutritiva de Manos, amb mel.\n"
   "• Crema Antiedad Manos y Uñas, amb àcid hialurònic.\n"
   "• Reparador Labios, amb pròpolis i àloe vera, per quan ja hi ha esquerdes.\n"
   "• Protector Labios, amb karité, per prevenir-les.\n\n"
   "Un truc: posa't la crema de mans just després d'eixugar-te-les, quan la pell encara està una mica humida.\n\n"
   f"{CTA}"),
  tags=["#cremademans", "#llavis", "#hivern", "#pellseca", "#dermocosmetica", "#cosmeticafarmacia"]),

 dict(id="P06", slug="mp-pell-seca", date="2026-12-08", time="19:00",
  title="Pell seca a l'hivern: de la dutxa a la crema",
  hook="Netejar sense assecar i hidratar cada dia.",
  products=[
   dict(code="FPBDO480S", name="Aceite de Ducha Protector", kind="COS", body="Oli de dutxa calmant i nutritiu per a pell molt seca i sensible. Neteja sense arrossegar els lípids de la pell. Format de llarga durada."),
   dict(code="FPICBL71S", name="Gel Baño Hidratante", kind="COS", body="Gel de bany calmant i dermoprotector per a pell seca i sensible. Format gran amb dosificador: fins a 420 polsacions."),
   dict(code="FPCCIC72S", name="Leche Corporal Hidratante Fuerte", kind="COS", body="Llet corporal amb àcid hialurònic i àcid lactobiònic. Textura rica i renovadora per a la pell més seca."),
   dict(code="FPCCLC72S", name="Loción Corporal Hidratante", kind="COS", body="Loció corporal amb àcid hialurònic i alvocat. Textura lleugera i tonificant per a l'ús diari."),
  ],
  caption=("🚿 Pell seca a l'hivern: de la dutxa a la crema\n\n"
   "A l'hivern la pell perd aigua més de pressa i la calefacció no hi ajuda. La rutina que proposem, tota de marca pròpia:\n\n"
   "1. Dutxa curta i tèbia amb l'Aceite de Ducha Protector (pell molt seca) o el Gel Baño Hidratante (pell seca i sensible).\n"
   "2. Hidratació just en sortir: Leche Corporal Hidratante Fuerte si la pell tiba molt, o Loción Corporal Hidratante si prefereixes una textura lleugera.\n\n"
   "Si la picor no marxa, hi ha plaques vermelles o esquerdes que sagnen, consulta el metge o el dermatòleg.\n\n"
   f"{CTA}"),
  tags=["#pellseca", "#hidratacio", "#hivern", "#dermocosmetica", "#pellsensible", "#cosmeticafarmacia"]),

 dict(id="P07", slug="mp-regal-osmotica", date="2026-12-12", time="12:00",
  title="Idea de regal: la rutina antiedat osmòtica",
  hook="Quatre passos amb Osmoshield® i Microceramid®.",
  products=[
   dict(code="FPCVOC35S", name="Crema Osmótica", kind="COS", body="Crema antiedat global de dia amb Osmoshield®, Microceramid® i complex Pro-Longevity. La base de la rutina."),
   dict(code="FPCVSO23S", name="Sérum Osmótico", kind="COS", body="Sèrum concentrat antiedat global. S'aplica abans de la crema, matí i nit, sobre la pell neta."),
   dict(code="FPCVOO15S", name="Contorno de Ojos Osmótico", kind="COS", body="Contorn d'ulls amb Osmoshield® i Microceramid® per a la zona més fina i delicada del rostre."),
   dict(code="FPCVOB33S", name="Crema Osmótica Noche", kind="COS", body="Crema de nit antiedat global amb Schisandra i complex Pro-Longevity. Per acabar el dia."),
  ],
  caption=("🎁 Idea de regal: la rutina antiedat osmòtica\n\n"
   "Si busques un regal que s'usi de debò, una rutina facial completa és una aposta segura. La línia osmòtica de marca pròpia té quatre passos:\n\n"
   "• Sérum Osmótico, matí i nit.\n"
   "• Crema Osmótica, de dia.\n"
   "• Crema Osmótica Noche, amb Schisandra.\n"
   "• Contorno de Ojos Osmótico.\n\n"
   "Es poden regalar junts o començar per un parell. Si no coneixes la pell de qui el rep, vine i t'ajudem a triar.\n\n"
   f"{CTA}"),
  tags=["#regalsdenadal", "#nadal", "#antiedat", "#rutinafacial", "#dermocosmetica", "#cosmeticafarmacia"]),

 dict(id="P08", slug="mp-descans", date="2026-12-15", time="19:00",
  title="Dormir millor en època de festes",
  hook="Melatonina en tres formats i una opció a base de plantes.",
  products=[
   dict(code="FPATMEZ2S", name="Melatonina Complex", kind="SUP", body="Comprimits amb melatonina, L-triptòfan i vitamina B6. 40 comprimits recoberts."),
   dict(code="FPMLGMZ1S", name="Melatonina Gummies", kind="SUP", body="Gominoles amb melatonina i passiflora, sense gluten ni sucres afegits. 50 gominoles."),
   dict(code="FPMLTS11S", name="Spray Melatonina Fast", kind="SUP", body="Melatonina en esprai amb gust de menta, pràctic per portar a sobre. Flascó de 10 ml."),
   dict(code="FPVLNTZ0S", name="Valero Natur", kind="SUP", body="Comprimits amb valeriana i passiflora PurePassicalm™. 30 comprimits recoberts."),
  ],
  caption=("🌙 Dormir millor en època de festes\n\n"
   "Sopars tard, horaris canviats, més pantalles… el son és el primer que se'n ressent al desembre. De marca pròpia tenim:\n\n"
   "• Melatonina Complex: melatonina amb L-triptòfan i vitamina B6.\n"
   "• Melatonina Gummies: en gominola, amb passiflora.\n"
   "• Spray Melatonina Fast: en esprai, per portar a sobre.\n"
   "• Valero Natur: valeriana i passiflora.\n\n"
   "La melatonina contribueix a reduir el temps necessari per adormir-se (prenent 1 mg poc abans d'anar al llit). Abans de res, però: horaris regulars, habitació fosca i pantalles fora una hora abans.\n\n"
   f"Si prens altres medicaments o l'insomni dura setmanes, parla'n amb el metge. {CTA}\n\n{LEGAL_SUP}"),
  tags=["#dormir", "#melatonina", "#insomni", "#descans", "#nadal", "#complementsalimentaris"]),

 dict(id="P09", slug="mp-cabell", date="2026-12-19", time="12:00",
  title="Cabell fort i cuidat",
  hook="Xampú, ampolles, complement i mascareta de marca pròpia.",
  products=[
   dict(code="FPIEFO81S", name="Champú Anticaída", kind="COS", body="Xampú fortificant amb adenosina i ortiga, de pH fisiològic. Per a l'ús freqüent en cabell amb tendència a caure."),
   dict(code="FPIEFCG1S", name="Ampollas Anticaída", kind="COS", body="Ampolles fortificants amb adenosina i Trichogen®. Caixa de 10 ampolles de 10 ml, per a un mes d'ús."),
   dict(code="FPACMTZ1S", name="Hair Formula Anticaída", kind="SUP", body="Càpsules amb cistina, metionina, oli de llavors de carbassa, biotina, vitamina E i minerals. 120 càpsules."),
   dict(code="FPIEMC62S", name="Mascarilla Capilar Reparadora", kind="COS", body="Mascareta capil·lar amb bioceramides i mantega de karité. Reforça i repara el cabell sec o castigat."),
  ],
  caption=("💇 Cabell fort i cuidat\n\n"
   "A la tardor és normal que caigui més cabell del compte: és estacional i es recupera. Mentrestant, la nostra línia de marca pròpia:\n\n"
   "• Champú Anticaída, amb adenosina i ortiga.\n"
   "• Ampollas Anticaída, amb adenosina i Trichogen®, per a un mes.\n"
   "• Hair Formula Anticaída, complement amb biotina, cistina i minerals.\n"
   "• Mascarilla Capilar Reparadora, per al cabell sec.\n\n"
   "La biotina i el zinc contribueixen al manteniment del cabell en condicions normals. Si la caiguda és sobtada, a clapes o va acompanyada d'altres símptomes, consulta el dermatòleg.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#cabell", "#caigudadelcabell", "#xampu", "#biotina", "#dermocosmetica", "#regalsdenadal"]),

 dict(id="P10", slug="mp-digestio-festes", date="2026-12-22", time="19:00",
  title="Àpats de festa, digestió tranquil·la",
  hook="Enzims, ferments, plantes i un producte per a l'acidesa.",
  products=[
   dict(code="FPAADTZ1S", name="Enzitasi", kind="SUP", body="Comprimits amb enzims digestius protegits (Digezyme®), calci i gingebre. 30 comprimits recoberts."),
   dict(code="FPAACOZ3S", name="Colitab Digest", kind="SUP", body="Càpsules amb enzims, L. acidophilus tindalitzat, passiflora, fonoll, comí i anís. 30 càpsules vegetals."),
   dict(code="FPAAEPZ1S", name="Epatotab", kind="SUP", body="Comprimits amb N-acetilcisteïna, silimarina fitosoma, carxofa (Cinarax®) i L-metionina. 30 comprimits recoberts."),
   dict(code="FPAAAAZ0S", name="Reflux Control", kind="PS", body="Comprimits masticables que redueixen el reflux gastroesofàgic, calmen la hiperacidesa i protegeixen la mucosa gàstrica. 24 comprimits."),
  ],
  caption=("🍽️ Àpats de festa, digestió tranquil·la\n\n"
   "Dinars llargs, sopars tard i més greix del compte. Per als dies de festa, de marca pròpia tenim:\n\n"
   "• Enzitasi: enzims digestius amb gingebre.\n"
   "• Colitab Digest: enzims, ferments i plantes carminatives (fonoll, comí, anís).\n"
   "• Epatotab: silimarina, carxofa i N-acetilcisteïna.\n"
   "• Reflux Control: comprimits masticables per al reflux i l'acidesa.\n\n"
   "I els consells de sempre: menjar a poc a poc, racions moderades i no estirar-se just després. Si l'acidesa és freqüent o hi ha dolor intens, vòmits o pèrdua de pes, consulta el metge.\n\n"
   f"{CTA}\n\n{LEGAL_PS} {LEGAL_SUP}"),
  tags=["#digestio", "#nadal", "#acidesa", "#reflux", "#festes", "#consellfarmaceutic"]),

 dict(id="P11", slug="mp-peus-cames", date="2026-12-29", time="19:00",
  title="Peus i cames després de tant caminar",
  hook="Talons secs, peus cansats i cames pesades.",
  products=[
   dict(code="FPCCCT51S", name="Crema Talones Urea 10%", kind="COS", body="Crema per a talons amb urea al 10% i ceramides, sense perfum. Acció reparadora intensiva per a talons secs i esquerdats."),
   dict(code="FPCCPS51S", name="Crema Pies Manteca de Karité", kind="COS", body="Crema de peus amb mantega de karité i extracte de farigola. Confort refrescant per a peus secs."),
   dict(code="FPCAGG52S", name="Gel Piernas Ginkgo Biloba", kind="COS", body="Gel per a cames cansades amb ginkgo biloba i escina. Desfatigant i tonificant, millor si es guarda a la nevera."),
   dict(code="FPAAVCZ1S", name="Vencap Plus", kind="SUP", body="Càpsules amb bioflavonoides, castanyer d'Índies, melilot i vitamina C. 30 càpsules."),
  ],
  caption=("🦶 Peus i cames després de tant caminar\n\n"
   "Compres, passejades, hores dret a la cuina… els peus i les cames ho noten. De marca pròpia:\n\n"
   "• Crema Talones Urea 10%: per a talons secs i esquerdats.\n"
   "• Crema Pies Manteca de Karité: hidratació i frescor diària.\n"
   "• Gel Piernas Ginkgo Biloba: per a la sensació de cames cansades.\n"
   "• Vencap Plus: complement amb castanyer d'Índies, melilot i vitamina C.\n\n"
   "Si notes una cama inflada, calenta o amb dolor sobtat, consulta el metge sense esperar. I si tens diabetis, qualsevol lesió al peu mereix una visita.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#peus", "#camescansades", "#talons", "#urea", "#dermocosmetica", "#consellfarmaceutic"]),

 dict(id="P12", slug="mp-esport", date="2027-01-02", time="12:00",
  title="Propòsit 2027: moure't més",
  hook="La línia DYNA de nutrició esportiva, ara de marca pròpia.",
  products=[
   dict(code="FPPENT80S", name="Proteína Whey Vitality", kind="SUP", body="Concentrat de proteïna de sèrum de llet amb inulina i probiòtics (B. subtilis i B. coagulans). 27 g de proteïna per dosi. Sabor neutre, xocolata o vainilla."),
   dict(code="FPCRTN60S", name="Creatina", kind="SUP", body="Creatina monohidrat Creapure®, sabor neutre. 60 dosis."),
   dict(code="FPABCAZ0S", name="Aminoácidos Esenciales BCAA", kind="SUP", body="Leucina, isoleucina i valina en proporció 4:1:1. 100 comprimits."),
   dict(code="FPAHMBZ0S", name="Activador HMB", kind="SUP", body="Hidroximetilbutirat 3000 mg per dosi. 100 comprimits."),
  ],
  caption=("🏃 Propòsit 2027: moure't més\n\n"
   "Si un dels propòsits és tornar a entrenar, la línia DYNA de marca pròpia t'acompanya:\n\n"
   "• Proteína Whey Vitality: 27 g de proteïna per dosi, amb fibra i probiòtics.\n"
   "• Creatina Creapure®: monohidrat de qualitat, sabor neutre.\n"
   "• Aminoácidos Esenciales BCAA 4:1:1.\n"
   "• Activador HMB 3000 mg.\n\n"
   "Les proteïnes contribueixen a augmentar i conservar la massa muscular, i la creatina augmenta el rendiment físic en sèries successives d'exercici breu d'alta intensitat (amb 3 g al dia).\n\n"
   f"Abans de començar, pregunta'ns: no tot serveix per a tothom, especialment si prens medicació o tens algun problema de ronyó. {CTA}\n\n{LEGAL_SUP}"),
  tags=["#esport", "#proteina", "#creatina", "#entrenament", "#nutricioesportiva", "#propositsanynou"]),

 dict(id="P13", slug="mp-boca", date="2027-01-05", time="19:00",
  title="Boca sana cada dia",
  hook="Dentifrici, col·lutoris i un gel per a les aftes.",
  products=[
   dict(code="FPITDE51S", name="Dentífrico Repair", kind="COS", body="Dentifrici amb àloe vera i àcid hialurònic per a la higiene diària de dents i genives sensibles."),
   dict(code="FPCACO61S", name="Colutorio Repair", kind="COS", body="Col·lutori sense alcohol amb àloe vera i àcid hialurònic. Acció filmògena i calmant. Flascó de 150 ml."),
   dict(code="FPCCLX61S", name="Colutorio Clorhexidina 0,2%", kind="COS", body="Col·lutori sense alcohol amb clorhexidina 0,2% (Clorex-A2G®), que redueix al mínim el risc de pigmentació. Per a ús puntual. Flascó de 200 ml."),
   dict(code="FPGAFT10S", name="Gel Afta Repair", kind="PS", body="Gel per a aftes i petites lesions de la cavitat oral, que ajuda a reduir ràpidament les molèsties. Tub amb aplicador."),
  ],
  caption=("🦷 Boca sana cada dia\n\n"
   "Després de les festes, la boca també agraeix tornar a la rutina. De marca pròpia tenim:\n\n"
   "• Dentífrico Repair: per a dents i genives sensibles.\n"
   "• Colutorio Repair: sense alcohol, calmant.\n"
   "• Colutorio Clorhexidina 0,2%: per a ús puntual, quan el dentista t'ho recomani.\n"
   "• Gel Afta Repair: per a les aftes que apareixen quan menys toca.\n\n"
   "Raspallat dues vegades al dia, fil dental i revisió anual al dentista: això no ho substitueix cap producte. Si una afta dura més de dues setmanes, cal que la vegi un professional.\n\n"
   f"{CTA}\n\n{LEGAL_PS}"),
  tags=["#salutbucal", "#dents", "#genives", "#aftes", "#dentifrici", "#consellfarmaceutic"]),

 dict(id="P14", slug="mp-flora", date="2027-01-09", time="12:00",
  title="Ferments làctics: la nostra gamma",
  hook="Quatre formats per a situacions diferents.",
  products=[
   dict(code="FPAAEF12S", name="Florafluid", kind="SUP", body="Flascons bevibles amb ferments tindalitzats i fructooligosacàrids. 10 flascons de 10 ml."),
   dict(code="FPATFTZ3S", name="Floratab", kind="SUP", body="Càpsules amb Saccharomyces cerevisiae var. boulardii CNCM I-3799, sense sucre ni lactosa. 24 càpsules."),
   dict(code="FPATFFX4S", name="Florafast", kind="SUP", body="Sobres stick amb Lactobacillus acidophilus La-14, Bifidobacterium lactis Bl-04 i fructooligosacàrids. 12 sobres."),
   dict(code="FPABFBZ0S", name="Bifi Bioma", kind="SUP", body="Càpsules a base de B. longum i B. lactis, en blíster d'ultraprotecció. Sense gluten ni lactosa."),
  ],
  caption=("🦠 Ferments làctics: la nostra gamma\n\n"
   "«Quin em va bé a mi?» és la pregunta més habitual quan parlem de ferments làctics. Depèn de per a què els vols, i per això en tenim quatre:\n\n"
   "• Florafluid: flascons bevibles, pràctics per a tota la família.\n"
   "• Floratab: amb llevat Saccharomyces boulardii.\n"
   "• Florafast: sobres stick amb dos ferments i fibra prebiòtica.\n"
   "• Bifi Bioma: bifidobacteris en blíster protector.\n\n"
   "Si t'han receptat un antibiòtic, pregunta'ns quan i com prendre'ls. I si tens diarrea amb febre, sang o que dura més de dos dies, consulta el metge.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#probiotics", "#fermentslactics", "#florintestinal", "#digestio", "#antibiotics", "#complementsalimentaris"]),

 dict(id="P15", slug="mp-magnesi-energia", date="2027-01-12", time="19:00",
  title="Gener amb energia",
  hook="Magnesi i multivitamínics de marca pròpia.",
  products=[
   dict(code="FPATMAX1S", name="Magnesium", kind="SUP", body="Sobres amb glicerofosfat i pidolat de magnesi, gust de taronja. 20 sobres."),
   dict(code="FPATMGZ0S", name="Magnesium Cap", kind="SUP", body="Càpsules amb magnesi sucrosomial, una forma pensada per a una bona tolerància. 30 càpsules."),
   dict(code="FPATMUZ1S", name="Multivit Cap", kind="SUP", body="Càpsules amb vitamines, luteïna i minerals. 30 càpsules."),
   dict(code="FPAMVEZ1S", name="Multivit efervescent", kind="SUP", body="Multivitamínic en comprimits efervescents. 20 comprimits."),
  ],
  caption=("⚡ Gener amb energia\n\n"
   "La costa de gener també es nota al cos: cansament, poca llum i horaris que tornen a la normalitat. De marca pròpia tenim:\n\n"
   "• Magnesium: sobres de gust de taronja.\n"
   "• Magnesium Cap: magnesi sucrosomial en càpsules.\n"
   "• Multivit Cap: vitamines, luteïna i minerals.\n"
   "• Multivit efervescent.\n\n"
   "El magnesi contribueix a disminuir el cansament i la fatiga. Però si el cansament és intens, dura setmanes o va acompanyat d'altres símptomes, val la pena una analítica: parla'n amb el metge.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#magnesi", "#energia", "#cansament", "#multivitaminic", "#gener", "#complementsalimentaris"]),

 dict(id="P16", slug="mp-facial-hidratacio", date="2027-01-16", time="12:00",
  title="Rutina facial d'hidratació",
  hook="Netejar, hidratar i il·luminar en quatre passos.",
  products=[
   dict(code="FPCVSM74S", name="Agua Micelar", kind="COS", body="Aigua micel·lar amb al·lantoïna que neteja i desmaquilla cara i ulls. Format gran per a tota la família."),
   dict(code="FPCVIF31S", name="Crema Hidratante Antiedad", kind="COS", body="Crema hidratant antiedat amb àcid hialurònic IaluDeep®. Textura rica, per a pell normal a seca."),
   dict(code="FPCVGI30S", name="Gel Hyaluronic 40%", kind="COS", body="Gel d'hidratació intensiva amb àcid hialurònic i vitamina E. Textura fresca que s'absorbeix de seguida."),
   dict(code="FPSFLA20S", name="Sérum Flash", kind="COS", body="Sèrum amb àcid hialurònic IaluDeep®. Lluminositat i efecte tensor immediat, ideal abans d'una ocasió especial."),
  ],
  caption=("💧 Rutina facial d'hidratació\n\n"
   "Al gener la pell de la cara demana aigua. Una rutina senzilla amb la nostra marca pròpia:\n\n"
   "1. Netejar amb l'Agua Micelar, matí i nit.\n"
   "2. Gel Hyaluronic 40% com a sèrum d'hidratació.\n"
   "3. Crema Hidratante Antiedad per segellar.\n"
   "4. Sérum Flash els dies que vols un efecte immediat.\n\n"
   "I de dia, sempre protecció solar, també a l'hivern.\n\n"
   f"{CTA}"),
  tags=["#rutinafacial", "#hidratacio", "#acidhialuronic", "#aiguamicelar", "#dermocosmetica", "#cosmeticafarmacia"]),

 dict(id="P17", slug="mp-articulacions", date="2027-01-19", time="19:00",
  title="Col·lagen i companyia",
  hook="Complements per a qui cuida articulacions i teixits.",
  products=[
   dict(code="FPAACL12S", name="Collagen Age Formula", kind="SUP", body="Flascons bevibles amb col·lagen Verisol®, àcid hialurònic Hyabest® i manganès. Sense gluten ni sucres. 20 flascons."),
   dict(code="FPARTOX0S", name="Nutriflex Complex", kind="SUP", body="Sobres amb col·lagen Fortigel®, vitamines K2, C, D3 i E i manganès. 20 sobres."),
   dict(code="FPLRNCZ0S", name="Hyaluskin", kind="SUP", body="Càpsules amb àcid hialurònic. Sense gluten. 60 càpsules."),
   dict(code="FPPSTKX0S", name="Boswellia Fast", kind="SUP", body="Sobres bucodispersables amb PEA micronitzada i boswèl·lia, gust de menta. 12 sobres."),
  ],
  caption=("🦴 Col·lagen i companyia\n\n"
   "El col·lagen és un dels complements que més ens demaneu. La nostra gamma de marca pròpia:\n\n"
   "• Collagen Age Formula: col·lagen Verisol® amb àcid hialurònic i manganès, en flascons.\n"
   "• Nutriflex Complex: col·lagen Fortigel® amb vitamines C, D3, K2 i E.\n"
   "• Hyaluskin: àcid hialurònic en càpsules.\n"
   "• Boswellia Fast: boswèl·lia i PEA en sobres bucodispersables.\n\n"
   "La vitamina C contribueix a la formació normal de col·lagen per al funcionament normal dels cartílags i de la pell, i el manganès a la formació normal del teixit connectiu. Si tens dolor articular persistent o inflamació, consulta el metge.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#collagen", "#articulacions", "#acidhialuronic", "#vitaminac", "#complementsalimentaris", "#benestar"]),

 dict(id="P18", slug="mp-bioma-control", date="2027-01-23", time="12:00",
  title="Pell grassa o amb imperfeccions",
  hook="La línia Bioma Control, en quatre passos.",
  products=[
   dict(code="FPCVDB63S", name="Gel Dermolimpiador Bioma Control", kind="COS", body="Gel netejador amb Probiotic-Balance i niacinamida. Purifica i regula el greix sense agredir la pell."),
   dict(code="FPSLAT60S", name="Tónico Bioma Control", kind="COS", body="Tònic amb àcids microexfoliants que minimitza els porus i regula el greix. Després de la neteja."),
   dict(code="FPCVCB33S", name="Fluido Matificante Bioma Control", kind="COS", body="Fluid hidratant matificant amb Probiotic-Balance i niacinamida. Textura lleugera per a pell grassa o mixta."),
   dict(code="FPCVTA22S", name="Stop-Granos Bioma Control", kind="COS", body="Aplicació localitzada amb Peptide 3Action. Acció ràpida sobre les imperfeccions puntuals."),
  ],
  caption=("✨ Pell grassa o amb imperfeccions\n\n"
   "Netejar massa fort empitjora les coses. La línia Bioma Control de marca pròpia treballa amb la pell, no contra ella:\n\n"
   "1. Gel Dermolimpiador, matí i nit.\n"
   "2. Tónico amb àcids microexfoliants.\n"
   "3. Fluido Matificante com a hidratant.\n"
   "4. Stop-Granos sobre les imperfeccions puntuals.\n\n"
   "Si l'acne és moderat o intens, deixa cicatrius o afecta l'estat d'ànim, el dermatòleg és qui ha de valorar-ho; nosaltres t'ajudem amb la rutina de neteja i hidratació.\n\n"
   f"{CTA}"),
  tags=["#pellgrassa", "#acne", "#imperfeccions", "#niacinamida", "#rutinafacial", "#dermocosmetica"]),

 dict(id="P19", slug="mp-intim", date="2027-01-26", time="19:00",
  title="Higiene íntima: un gel per a cada moment",
  hook="Tres pH diferents i un complement amb lactobacils.",
  products=[
   dict(code="FPICDI61S", name="Gel Íntimo Fisiológico pH 5,5", kind="COS", body="Gel d'higiene íntima diària amb liquen i calèndula. El de cada dia."),
   dict(code="FPICDL60S", name="Gel Íntimo Calmante pH 6,5", kind="COS", body="Gel íntim delicat i protector amb malva i bisabolol. Per a èpoques de sensibilitat o sequedat."),
   dict(code="FPICDA60S", name="Gel Íntimo Activo pH 4,5", kind="COS", body="Gel íntim purificant i antiolor amb ferments làctics biolisats. Per a quan cal una neteja més activa."),
   dict(code="FPAUROZ1S", name="Gynobioma", kind="SUP", body="Càpsules vegetals amb L. acidophilus, L. gasseri i L. rhamnosus. Sense gluten ni lactosa. 30 càpsules."),
  ],
  caption=("🌸 Higiene íntima: un gel per a cada moment\n\n"
   "No tots els gels íntims són iguals: el pH canvia segons l'edat i el moment. De marca pròpia tenim:\n\n"
   "• Gel Íntimo Fisiológico pH 5,5: per a cada dia.\n"
   "• Gel Íntimo Calmante pH 6,5: per a èpoques de sensibilitat o sequedat.\n"
   "• Gel Íntimo Activo pH 4,5: purificant i antiolor.\n"
   "• Gynobioma: complement amb tres lactobacils.\n\n"
   "Picor intensa, molèsties que no marxen o fluix diferent de l'habitual: consulta el metge o el ginecòleg abans de provar res pel teu compte.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#higieneintima", "#salutfemenina", "#dona", "#lactobacils", "#cosmeticafarmacia", "#consellfarmaceutic"]),

 dict(id="P20", slug="mp-baby", date="2027-01-30", time="12:00",
  title="Línia baby i infantil",
  hook="Per al bany, el bolquer i els primers complements.",
  products=[
   dict(code="FPICBB72S", name="Gel de Baño Baby", kind="COS", body="Gel de bany amb al·lantoïna i oli de cotó que neteja suaument cos i cabell. Format amb dosificador."),
   dict(code="FPCABP52S", name="Pasta Óxido de Zinc 20%", kind="COS", body="Pasta a l'aigua amb òxid de zinc al 20% i oli de cotó. Protegeix i calma la pell envermellida de la zona del bolquer."),
   dict(code="FPAAFG11S", name="Flora Gotas Baby", kind="SUP", body="Gotes amb Lactobacillus rhamnosus HN001 i Bifidobacterium lactis HN019, gust neutre. Flascó de 5,4 ml."),
   dict(code="FPAADJZ2S", name="DHA Junior", kind="SUP", body="Perletes masticables amb DHA, EPA i vitamina D3, pensades per als més petits."),
  ],
  caption=("🧸 Línia baby i infantil\n\n"
   "Per als més petits de casa, la nostra marca pròpia té:\n\n"
   "• Gel de Baño Baby: cos i cabell, amb al·lantoïna i oli de cotó.\n"
   "• Pasta Óxido de Zinc 20%: per protegir la zona del bolquer.\n"
   "• Flora Gotas Baby: ferments làctics en gotes de gust neutre.\n"
   "• DHA Junior: perletes masticables amb DHA, EPA i vitamina D3.\n\n"
   "En nadons i infants, qualsevol complement sempre amb el consell del pediatre o el nostre. I si una irritació del bolquer no millora en pocs dies o té aspecte diferent, que ho vegi el pediatre.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#nadons", "#baby", "#bolquer", "#infants", "#pediatria", "#cosmeticafarmacia"]),

 dict(id="P21", slug="mp-estres", date="2027-02-02", time="19:00",
  title="Èpoques d'estrès",
  hook="Plantes adaptògenes i vitamines del grup B.",
  products=[
   dict(code="FPARDLZ2S", name="Stresstab", kind="SUP", body="Comprimits amb ashwagandha i rhodiola. 30 comprimits recoberts."),
   dict(code="FPARDLZ1S", name="Rhodiola", kind="SUP", body="Comprimits amb Rhodiola rosea (Rhodiolife®). 30 comprimits."),
   dict(code="FPRLAXZ0S", name="Relax Cap", kind="SUP", body="Càpsules amb lavanda, safrà, vitamina B6 i oli de perilla. 14 càpsules."),
   dict(code="FPAABUZ1S", name="B Ultra", kind="SUP", body="Càpsules vegetals amb vitamines del grup B. 30 càpsules."),
  ],
  caption=("🧘 Èpoques d'estrès\n\n"
   "Exàmens, tancaments, cures de familiars… hi ha temporades que pesen. De marca pròpia tenim:\n\n"
   "• Stresstab: ashwagandha i rhodiola.\n"
   "• Rhodiola: extracte de Rhodiola rosea.\n"
   "• Relax Cap: lavanda, safrà i vitamina B6.\n"
   "• B Ultra: vitamines del grup B.\n\n"
   "La vitamina B6 contribueix al funcionament normal del sistema nerviós i a la funció psicològica normal. Però si l'ansietat o el desànim duren setmanes o t'impedeixen fer vida normal, parla'n amb el metge: demanar ajuda és el primer pas, i no n'hi ha cap que sigui petit.\n\n"
   f"Si prens antidepressius, ansiolítics o altres medicaments, consulta'ns abans de prendre cap planta. {CTA}\n\n{LEGAL_SUP}"),
  tags=["#estres", "#ashwagandha", "#rhodiola", "#vitaminab", "#benestaremocional", "#complementsalimentaris"]),

 dict(id="P22", slug="mp-pell-sensible", date="2027-02-06", time="12:00",
  title="Pell sensible i amb vermellors",
  hook="La línia Bioma Confort reforça la barrera cutània.",
  products=[
   dict(code="FPCVCM34S", name="Crema Anti-Rojeces Bioma Confort", kind="COS", body="Crema amb Prebiotic-Defence i troxerutina per a pell amb tendència a la cuperosi i les vermellors."),
   dict(code="FPCICO31S", name="Fluido Bioma Confort", kind="COS", body="Fluid amb Pre+Probiotic Complex i magnòlia que reforça la barrera cutània. Textura lleugera."),
   dict(code="FPCNIC30S", name="Sérum Bioma Confort", kind="COS", body="Sèrum amb Pre+Probiotic Complex i Isopalmide® per a la pell reactiva. S'aplica abans de la crema."),
   dict(code="FPCVTL64S", name="Tónico Bioma Confort", kind="COS", body="Tònic amb Prebiotic-Defence i nabiu que calma, hidrata i refresca."),
  ],
  caption=("🌿 Pell sensible i amb vermellors\n\n"
   "Fred fora, calefacció dins: la pell reactiva ho passa malament al febrer. La línia Bioma Confort de marca pròpia:\n\n"
   "1. Tónico Bioma Confort, després de la neteja.\n"
   "2. Sérum Bioma Confort, per a la pell reactiva.\n"
   "3. Fluido Bioma Confort o Crema Anti-Rojeces, segons si tens tendència a la cuperosi.\n\n"
   "Pocs productes, sense perfum fort i sense canviar de rutina cada setmana: la pell sensible agraeix la constància. Si les vermellors persisteixen o hi ha granets, consulta el dermatòleg.\n\n"
   f"{CTA}"),
  tags=["#pellsensible", "#vermellors", "#cuperosi", "#rutinafacial", "#dermocosmetica", "#cosmeticafarmacia"]),

 dict(id="P23", slug="mp-serums", date="2027-02-09", time="19:00",
  title="Sèrums d'actius purs",
  hook="Vitamina C, niacinamida, retinol i pèptids: quin i quan.",
  products=[
   dict(code="FPCAVC20S", name="Vitamina C 20%", kind="COS", body="Sèrum amb vitamina C al 20%, per al matí. Lluminositat i to uniforme. Sempre amb protecció solar a sobre."),
   dict(code="FPANIA10S", name="Niacinamida 10%", kind="COS", body="Sèrum amb niacinamida al 10%. Per a porus visibles, greix i to irregular. Matí o nit."),
   dict(code="FPCAVA21S", name="Sérum Noche Retinol 0,3% Puro", kind="COS", body="Sèrum de nit amb retinol pur al 0,3%. Retexturitzant global i antiarrugues. Cal introduir-lo de manera progressiva."),
   dict(code="FPCAAR21S", name="Polipéptidos 10%", kind="COS", body="Sèrum amb polipèptids al 10%, per a fermesa. Combina bé amb la resta d'actius, matí i nit."),
  ],
  caption=("🧪 Sèrums d'actius purs\n\n"
   "Els sèrums d'actius purs de marca pròpia funcionen, però cal saber combinar-los:\n\n"
   "• Vitamina C 20%: al matí, i protecció solar a sobre.\n"
   "• Niacinamida 10%: matí o nit, per a porus i greix.\n"
   "• Sérum Noche Retinol 0,3%: només de nit, començant dues nits per setmana.\n"
   "• Polipéptidos 10%: fermesa, matí i nit.\n\n"
   "El retinol no és per a tothom: no es recomana durant l'embaràs ni la lactància, i cal evitar barrejar-lo la mateixa nit amb àcids. Si tens dubtes, vine amb el que ja fas servir i t'ho ordenem.\n\n"
   f"{CTA}"),
  tags=["#serum", "#vitaminac", "#niacinamida", "#retinol", "#rutinafacial", "#dermocosmetica"]),

 dict(id="P24", slug="mp-per-a-ell", date="2027-02-13", time="12:00",
  title="Per a ell",
  hook="Quatre bàsics d'higiene i cosmètica masculina.",
  products=[
   dict(code="FPCRIU30S", name="Crema Men Hidratante", kind="COS", body="Crema hidratant masculina amb àcid hialurònic IaluDeep®. Reforça i protegeix, textura que no deixa brillantor."),
   dict(code="FPCVCU31S", name="Gel Men Total", kind="COS", body="Gel multiús amb àcid hialurònic que calma i tonifica, també després de l'afaitat."),
   dict(code="FPCVBA60S", name="Crema de Afeitar", kind="COS", body="Crema d'afaitar amb àloe i al·lantoïna. Calma i hidrata, pensada per a pells sensibles."),
   dict(code="FPIDDT30S", name="Deo Roll-On Antitranspirante", kind="COS", body="Desodorant roll-on antitranspirant, 0% alcohol. Per a l'ús diari."),
  ],
  caption=("🎁 Per a ell\n\n"
   "Sant Valentí és demà i un neceser ben pensat sempre encerta. De marca pròpia, quatre bàsics:\n\n"
   "• Crema Men Hidratante, amb àcid hialurònic.\n"
   "• Gel Men Total, per a després de l'afaitat.\n"
   "• Crema de Afeitar, per a pells sensibles.\n"
   "• Deo Roll-On Antitranspirante, sense alcohol.\n\n"
   "I si és per a tu mateix, també val. Les rutines curtes són les que es compleixen.\n\n"
   f"{CTA}"),
  tags=["#santvalenti", "#regal", "#cosmeticamasculina", "#afaitat", "#dermocosmetica", "#cosmeticafarmacia"]),

 dict(id="P25", slug="mp-omega-q10", date="2027-02-16", time="19:00",
  title="Omega-3 i coenzim Q10",
  hook="Tres complements que sovint ens demaneu junts.",
  products=[
   dict(code="FPAMOMZ2S", name="Omega 3", kind="SUP", body="Càpsules d'oli de peix purificat, titulat en EPA i DHA. Sense gluten."),
   dict(code="FPAACZZ1S", name="Coenzima Q10", kind="SUP", body="Càpsules softgel amb coenzim Q10, vitamina E i oli d'oliva verge extra. 30 càpsules."),
   dict(code="FPUBICZ0S", name="Ubiquinol 100", kind="SUP", body="Càpsules softgel amb ubiquinol, la forma reduïda del coenzim Q10. 30 càpsules."),
  ],
  caption=("🐟 Omega-3 i coenzim Q10\n\n"
   "Tres complements de marca pròpia que sovint ens demaneu junts:\n\n"
   "• Omega 3: oli de peix purificat, ric en EPA i DHA.\n"
   "• Coenzima Q10: amb vitamina E i oli d'oliva verge extra.\n"
   "• Ubiquinol 100: la forma reduïda del Q10.\n\n"
   "L'EPA i el DHA contribueixen al funcionament normal del cor (amb una ingesta diària de 250 mg). Si prens anticoagulants, antiagregants o medicació per al colesterol, consulta'ns abans: hi ha combinacions que cal vigilar.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#omega3", "#coenzimq10", "#ubiquinol", "#cor", "#complementsalimentaris", "#consellfarmaceutic"]),

 dict(id="P26", slug="mp-benestar-femeni", date="2027-02-20", time="12:00",
  title="Benestar femení",
  hook="Menopausa, vies urinàries i ossos: la nostra selecció.",
  products=[
   dict(code="FPAAMTZ0S", name="Feminic Menopausia", kind="SUP", body="Comprimits amb Cimicifuga racemosa i passiflora PurePassicalm™. 30 comprimits ranurats."),
   dict(code="FPAUDFX1S", name="Uratab Prev", kind="SUP", body="Sobres amb nabiu vermell (Berry Defence®), D-manosa i vitamina C. Gust de fruits vermells. 14 sobres."),
   dict(code="FPAAUTZ4S", name="Uratab", kind="SUP", body="Fórmula potenciada amb Larixicina®, gaiuba, orenga i vitamina B2. 20 comprimits bicapa d'alliberament controlat."),
   dict(code="FPD3K2Z0S", name="Vit D3+K2", kind="SUP", body="Càpsules amb vitamina D3 i vitamina K2 (K2Vital®). Sense gluten ni lactosa. 60 càpsules."),
  ],
  caption=("💜 Benestar femení\n\n"
   "Una selecció de marca pròpia per a tres moments diferents:\n\n"
   "• Feminic Menopausia: cimicífuga i passiflora.\n"
   "• Uratab Prev: nabiu vermell i D-manosa, per prevenir.\n"
   "• Uratab: fórmula potenciada amb gaiuba i orenga.\n"
   "• Vit D3+K2: vitamina D3 amb K2.\n\n"
   "La vitamina D contribueix al manteniment dels ossos en condicions normals. Molèsties urinàries amb febre, sang a l'orina o dolor lumbar són motiu de visita al metge, no d'automedicació.\n\n"
   f"{CTA}\n\n{LEGAL_SUP}"),
  tags=["#salutfemenina", "#menopausa", "#cistitis", "#vitaminad", "#dona", "#complementsalimentaris"]),

 dict(id="P27", slug="mp-ulls", date="2027-02-23", time="19:00",
  title="Ulls cansats, mirada descansada",
  hook="Pantalles, calefacció i poques hores de son es noten als ulls.",
  products=[
   dict(code="FPGOHY11S", name="Eye Drops 0,2%", kind="PS", body="Gotes oculars hidratants i lubricants amb àcid hialurònic al 0,2%. Compatibles amb lents de contacte. 10 ampolles monodosi."),
   dict(code="FPCSLOG2S", name="Toallitas Oculares", kind="PS", body="Tovalloletes oculars amb extracte de malva i hialuronat de sodi, aptes per a nadons. 24 tovalloletes."),
   dict(code="FPCVCC22S", name="Gel Crema Bolsas y Ojeras", kind="COS", body="Gel crema per a bosses i ulleres amb centella asiàtica i pèptids. Efecte fresc al matí."),
   dict(code="FPCVOL11S", name="Contorno de Ojos y Labios", kind="COS", body="Contorn d'ulls i llavis amb àcid hialurònic IaluDeep®. Acció antiarrugues intensiva."),
  ],
  caption=("👀 Ulls cansats, mirada descansada\n\n"
   "Hores de pantalla, calefacció i poc son: els ulls són els primers a queixar-se. De marca pròpia tenim:\n\n"
   "• Eye Drops 0,2%: gotes hidratants en monodosi, aptes amb lents de contacte.\n"
   "• Toallitas Oculares: per netejar les parpelles, també en nadons.\n"
   "• Gel Crema Bolsas y Ojeras: amb centella i pèptids.\n"
   "• Contorno de Ojos y Labios: antiarrugues amb àcid hialurònic.\n\n"
   "Ull vermell amb dolor, visió borrosa sobtada o secreció: consulta l'oftalmòleg o el metge sense esperar.\n\n"
   f"{CTA}\n\n{LEGAL_PS}"),
  tags=["#ulls", "#ullsec", "#pantalles", "#contornulls", "#consellfarmaceutic", "#dermocosmetica"]),
]
