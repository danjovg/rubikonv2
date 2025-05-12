const ctx = document.getElementById('graficaVentas');
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    datasets: [{
      label: 'Ventas (Q)',
      data: [12000, 14000, 10000, 17000, 20000],
      backgroundColor: 'rgba(59, 130, 246, 0.6)'
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Ventas por mes' }
    }
  }
});
