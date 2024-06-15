<template>
  <div class="container mx-auto px-0">
    <button class="retour">
      <svg class="h-6 w-6 mr-2 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M15 19l-7-7 7-7"></path>
      </svg>
      Retour
    </button>
    <h1 class="create_account">Créer un compte</h1>
    <form @submit.prevent="submitForm" class="form-group">
      <label for="first-name">Prénom</label>
      <input type="text" placeholder="Ex : Mustafa" id="first-name" v-model="firstName" />

      <br /><br />
      <label for="last-name" class="name pt-30">Nom</label>
      <input type="text" placeholder="Ex : Sak" id="last-name" v-model="lastName" />

      <div class="sm:col-span-3">
        <br />
        <label for="birth-day" class="block text-sm font-medium leading-6 text-gray-900">Date de naissance</label>
        <div class="grid grid-cols-3 gap-2">
          <div class="relative">
            <select id="birth-day" name="birth-day" class="select-input" v-model="selectedDay">
              <option value="" disabled selected class="placeholder-option">Jour</option>
              <option v-for="day in days" :key="day">{{ day }}</option>
            </select>
            <svg class="h-4 w-4 absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </div>

          <div class="relative">
            <select id="birth-month" name="birth-month" class="select-input" v-model="selectedMonth">
              <option value="" disabled selected class="placeholder-option">Mois</option>
              <option v-for="(month, index) in months" :key="index + 1">{{ index + 1 }}</option>
            </select>
            <svg class="h-4 w-4 absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </div>

          <div class="relative">
            <select id="birth-year" name="birth-year" class="select-input" v-model="selectedYear">
              <option value="" disabled selected class="placeholder-option">Année</option>
              <option v-for="(year, index) in years" :key="year">{{ year }}</option>
            </select>
            <svg class="h-4 w-4 absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </div>
        </div>
      </div>
      <br />
      <label for="phone-number" class="pt-30">Numéro de téléphone</label>
      <input type="tel" placeholder="Ex : 06 51 11 97 75" id="phone-number" v-model="phoneNumber" />

      <label class="checkbox-label">
        <input type="checkbox" class="small-checkbox" v-model="receiveNews" />
        Je souhaite recevoir par e-mail des actualités sur ce service et ses partenaires.
      </label>
      <button type="submit" class="btn-primary">Accepter et continuer</button>
    </form>
    <h1 class="politics">En cliquant sur <span class="text-gray-700 font-bold">Accepter et Continuer</span>, J'accepte les 
      <span class="underline">Conditions Générales d'utilisation</span> et je reconnais avoir pris connaissance de la <span class="underline">Politique de confidentialité</span>.</h1>
  </div>
  <footer class="fixed-footer">
    <div class="footer-item">
      <svg class="h-6 w-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-4a7 7 0 1 0-14 0 7 7 0 0 0 14 0z"></path>
      </svg>
      <span>Rechercher</span>
    </div>
    <div class="footer-item">
      <svg class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14c-3.87 0-7-3.13-7-7 0-3.87 3.13-7 7-7 3.87 0 7 3.13 7 7 0 3.87-3.13 7-7 7zm0 2c-5.25 0-9.6 3.71-10.86 8.64-.14.56.27 1.36.86 1.36h20c.59 0 1-.8.86-1.36C21.6 19.71 17.25 16 12 16z"></path>
      </svg>
      <span>Compte</span>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'App',
  setup() {
    const firstName = ref('');
    const lastName = ref('');
    const selectedDay = ref<number | null>(null);
    const selectedMonth = ref<number | null>(null);
    const selectedYear = ref<number | null>(null);
    const phoneNumber = ref('');
    const receiveNews = ref(false);
    const days = Array.from({ length: 31 }, (_, i) => i + 1);
    const months = Array.from({ length: 12 }, (_, i) => i + 1);
    const years = Array.from({ length: 126 }, (_, i) => 1900 + i);

    const submitForm = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/users', {
          first_name: firstName.value,
          last_name: lastName.value,
          birth_day: selectedDay.value,
          birth_month: selectedMonth.value,
          birth_year: selectedYear.value,
          phone_number: phoneNumber.value,
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    return {
      firstName,
      lastName,
      selectedDay,
      selectedMonth,
      selectedYear,
      phoneNumber,
      receiveNews,
      days,
      months,
      years,
      submitForm,
    };
  },
});
</script>