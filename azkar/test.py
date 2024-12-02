import pandas as pd

# Create a data structure for the full Azkar table
data = {
    "Category": [
        "Morning Azkar", "Morning Azkar", "Morning Azkar", "Evening Azkar", "Evening Azkar", "Before Sleeping",
        "Before Sleeping", "Upon Waking Up", "Before Eating", "After Eating"
    ],
    "Show Before": [
        "In the name of God, the most gracious, the most merciful", 
        "Recite Surah Al-Ikhlas three times", 
        "Recite Surah Al-Falaq three times",
        "Recite Surah Al-Ikhlas three times", 
        "Recite Surah Al-Falaq three times", 
        "Say this before sleeping",
        "Recite Tasbih: Subhanallah (33x), Alhamdulillah (33x), Allahu Akbar (34x)", 
        "Say this when you wake up", 
        "Say this before eating", 
        "Say this after finishing your meal"
    ],
    "Transliteration": [
        "Allahu la ilaha illa Huwa, Al-Hayyul-Qayyum. La ta’khudhuhu sinatun wa la nawm. Lahu ma fi as-samawati wa ma fi al-ard. Man dha alladhi yashfa‘u ‘indahu illa bi-idhnih. Ya‘lamu ma bayna aydihim wa ma khalfahum, wa la yuhituna bishay’in min ‘ilmihi illa bima sha’a. Wasi‘a kursiyyuhu as-samawati wa al-ard, wa la ya’uduhu hifdhuhuma, wa Huwa Al-‘Aliyyu Al-‘Adheem.",
        "Qul Huwa Allahu Ahad. Allahus-Samad. Lam yalid wa lam yulad. Wa lam yakun lahu kufuwan ahad.", 
        "Qul A‘udhu Bi-Rabbil-Falaq. Min sharri ma khalaq. Wa min sharri ghasiqin idha waqab. Wa min sharri an-naffathati fi al-‘uqad. Wa min sharri hasidin idha hasad.",
        "Qul Huwa Allahu Ahad. Allahus-Samad. Lam yalid wa lam yulad. Wa lam yakun lahu kufuwan ahad.", 
        "Qul A‘udhu Bi-Rabbil-Falaq. Min sharri ma khalaq. Wa min sharri ghasiqin idha waqab. Wa min sharri an-naffathati fi al-‘uqad. Wa min sharri hasidin idha hasad.", 
        "Bismika Rabbi wada‘tu janbi, wa bika arfa‘uh. In amsakta nafsi faghfir laha, wa in arsaltaha fahfadhha bima tahfadhu bihi ‘ibadaka as-saliheen.", 
        "Subhanallah (33x), Alhamdulillah (33x), Allahu Akbar (34x)", 
        "Alhamdulillahi alladhi ahyana ba‘da ma amatana wa ilayhi an-nushur.", 
        "Bismillah.", 
        "Alhamdulillahilladhi at‘amana wa saqana wa ja‘alana muslimin."
    ],
    "Translation": [
        "Allah! There is no deity but Him, the Ever-Living, the Sustainer of existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is [presently] before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.",
        "Say: He is Allah, [Who is] One. Allah, the Eternal Refuge. He neither begets nor is born, nor is there to Him any equivalent.",
        "Say: I seek refuge in the Lord of daybreak, from the evil of that which He created, from the evil of darkness when it settles, from the evil of blowers in knots, and from the evil of an envier when he envies.",
        "Say: He is Allah, [Who is] One. Allah, the Eternal Refuge. He neither begets nor is born, nor is there to Him any equivalent.",
        "Say: I seek refuge in the Lord of daybreak, from the evil of that which He created, from the evil of darkness when it settles, from the evil of blowers in knots, and from the evil of an envier when he envies.",
        "In Your name, my Lord, I lay down my side, and in Your name, I rise. If You take my soul, then forgive it, and if You send it back, then protect it as You protect Your righteous servants.",
        "Glory is to Allah (33x), Praise is to Allah (33x), Allah is the Greatest (34x).",
        "Praise be to Allah, who gave us life after He caused us to die, and to Him is the return.",
        "In the name of Allah.",
        "Praise be to Allah who has fed us and given us drink, and made us Muslims."
    ],
    "Show After": [
        "(Surah Al-Baqarah 2:255)", 
        "(Recite 3 times)", 
        "(Recite 3 times)", 
        "(Recite 3 times)", 
        "(Recite 3 times)", 
        "(Before Sleeping)", 
        "(Before Sleeping)", 
        "(Upon Waking Up)", 
        "(Before Eating)", 
        "(After Eating)"
    ],
    "Reward": [
        "Whoever recites Ayat al-Kursi in the morning will be under Allah’s protection and guidance until the evening.",
        "Protects from harm and grants immense reward.",
        "Protects from harm and grants immense reward.",
        "Protects from harm and grants immense reward.",
        "Protects from harm and grants immense reward.",
        "Ensures forgiveness and protection overnight.",
        "Brings peace and blessings before sleeping.",
        "Shows gratitude to Allah and reminds of resurrection.",
        "Brings blessings to the food.",
        "Brings gratitude and blessings."
    ],
    "Count": [
        1, 3, 3, 3, 3, 1, 1, 1, 1, 1
    ]
}

# Convert data to a DataFrame
azkar_df = pd.DataFrame(data)

# Display the table to the user
print(azkar_df)