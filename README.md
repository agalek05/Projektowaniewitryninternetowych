# 🔬 Platforma Parazytologiczna - Analiza UX (User Experience)

Niniejszy dokument zawiera szczegółową analizę doświadczeń użytkownika (UX) dla systemu autentykacji oraz modułu bezpiecznego przesyłania obrazów mikroskopowych w architekturze typu One-Page (Single-Page Experience).

---

## 1. Architektura Informacji i Przepływ Użytkownika (User Flow)

Projekt interfejsu opiera się na strategii **One-Page Layout**, co eliminuje zbędne przeładowania stron i redukuje próg wejścia dla person badawczych (laborantów, parazytologów). 


## 2. Analiza Heurystyczna (wg 10 Heurystyk Nielsena)

### 🔴 1. Widoczność statusu systemu (Visibility of system status)
*   **Zastosowanie:** System natychmiastowo informuje użytkownika o jego stanie za pomocą dynamicznego paska diagnostycznego:
    *   Kolor czerwony (`#f8d7da`): Jasny komunikat *„Stan: Niezalogowany (Zaloguj się poniżej, aby odblokować system)”*.
    *   Kolor zielony (`#d1e7dd`): Komunikat *„Jesteś poprawnie zalogowany jako: [nazwa]”*.
*   **Wniosek UX:** Użytkownik nigdy nie czuje się zagubiony i dokładnie wie, dlaczego niektóre funkcje (np. wybór pliku) są w danym momencie zablokowane.

### 🔴 2. Dopasowanie systemu do świata rzeczywistego (Match between system and the real world)
*   **Zastosowanie:** Formularz przesyłania plików wykorzystuje natywny i powszechnie zrozumiały dla użytkowników systemowych standard interfejsu (`<input type="file">`). Etykiety i przyciski akcji sformułowane są w prostym, bezpośrednim języku (*„Wybierz plik graficzny z dysku”*, *„Wgraj zdjęcie do bazy danych”*).

### 🔴 3. Zapobieganie błędom (Error prevention)
*   **Zastosowanie:** 
    *   Ukrycie formularza uploadu przed osobami niezalogowanymi całkowicie eliminuje błędy autentykacji po stronie serwera (np. błędy typu `AnonymousUser ValueError`).
    *   Zastosowanie atrybutów `required` w polach formularza logowania blokuje wysyłanie pustych żądań HTTP przed interakcją z bazą danych.

---

## 3. Dostosowanie do Standardów Dostępności (Accessibility / WCAG)

Interfejs został zaprojektowany z myślą o pracy w warunkach laboratoryjnych, gdzie kontrast i czytelność tekstu są kluczowe:

*   **Kontrast i Kolorystyka (WCAG AA):** Tło paska dla zalogowanego użytkownika (ciemnozielony tekst `#0f5132` na jasnozielonym tle `#d1e7dd`) oraz dla niezalogowanego (ciemnoczerwony tekst `#842029` na jasnoczerwonym tle `#f8d7da`) spełniają rygorystyczne wymogi współczynnika kontrastu (minimum 4.5:1), co zapewnia pełną czytelność.
*   **Semantyka HTML5:** Zastosowanie znaczników `<main>`, `<section>`, `<article>` oraz `<header>` ułatwia nawigację osobom korzystającym z czytników ekranu (Screen Readers).
*   **Dostępność Formularzy:** Każde pole tekstowe posiada unikalny identyfikator (`id`) powiązany bezpośrednio z etykietą za pomocą atrybutu `for="id_..."`, co ułatwia interakcję dotykową i myszką.

---

## 4. Optymalizacja Wydajnościowa (Wydajność UX / Web Vitals)

*   **Brak Skakania Układu (CLS = 0):** W sekcji galerii zdjęć znaczniki `<img>` posiadają zdefiniowane sztywne proporcje za pomocą kontenera `.zdjecie-wrapper { padding-top: 75%; }`. Zapobiega to tzw. *Cumulative Layout Shift* (przesuwaniu się elementów strony w dół podczas ładowania się obrazków z bazy danych), co dramatycznie podnosi komfort przeglądania.
*   **Asynchroniczność i Lazy Loading:** Obrazy w galerii posiadają atrybut `loading="lazy"`. Przeglądarka pobiera pliki z bazy danych dopiero w momencie, gdy użytkownik przewinie stronę do sekcji galerii, oszczędzając pakiet danych i przyspieszając ładowanie strony startowej.

---

## 5. Rekomendacje i Dalsze Kroki UX (Future Roadmap)

Mimo wysokiej użyteczności obecnego rozwiązania, w kolejnych iteracjach projektu zaleca się wdrożenie następujących usprawnień:

1.  **Obsługa Drag & Drop:** Zastąpienie standardowego przycisku wyboru pliku interaktywną strefą zrzutu (Drag and Drop), co pozwoli użytkownikom na bezpośrednie przeciąganie zdjęć mikroskopowych z folderów systemowych.
2.  **Podgląd obrazu przed wysłaniem (Client-side Preview):** Wdrożenie prostego skryptu JavaScript, który wyświetli miniaturkę wybranego zdjęcia parazytologicznego jeszcze przed kliknięciem przycisku „Wgraj zdjęcie”, dając użytkownikowi pewność, że wybrał właściwy plik.
3.  **Wskaźnik progresu (Progress Bar):** Przy przesyłaniu plików o bardzo dużej rozdzielczości (częsty przypadek w fotografii medycznej/naukowej), dodanie paska postępu zapobiegnie wrażeniu, że strona zawiesiła się podczas wysyłania formularza.
