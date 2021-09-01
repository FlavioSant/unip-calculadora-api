const API_URL = "http://localhost:8000/api/v1/calculator";

const calcForm = document.getElementById("calculator");
const statisticForm = document.getElementById("statistic");

// Consulta na API
const getResult = async (apiURL, data, isStatistics = false) => {
  const formProps = Object.fromEntries(new FormData(data));

  const parsedBody = isStatistics
    ? {
        ...formProps,
        values: formProps.values.split(",").map((value) => Number(value)),
      }
    : formProps;

  return fetch(apiURL, {
    method: "POST",
    body: JSON.stringify(parsedBody),
  })
    .then((response) => response.json())
    .then((data) => data)
    .catch((err) => console.error(err));
};

// Submit do formulário de cálculos simples
calcForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const { resultado } = await getResult(API_URL, e.target);

  if (resultado) {
    alert(`Resultado = ${resultado}`);
  }
});

// Submit do formulário de cálculos estatísticos
statisticForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const { resultado } = await getResult(
    `${API_URL}/statistics`,
    e.target,
    true
  );

  if (resultado) {
    alert(`Resultado = ${resultado}`);
  }
});
