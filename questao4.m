% Número total de pontos (n) gerados para a simulação
N_total = 10000;

% Gerando N_total pares (x_k, y_k) de números aleatórios no intervalo [0, 1]
x = rand(1, N_total);
y = rand(1, N_total);

% Verificando o número (m) de pontos no primeiro quadrante do círculo unitário.
% A condição matemática para estar dentro do círculo é x^2 + y^2 <= 1.
pontos_dentro = (x.^2 + y.^2) <= 1;

% Contando os acertos acumulados (m) para cada passo da sucessão
m = cumsum(pontos_dentro);
n_vetor = 1:N_total;

% Calculando a sucessão de aproximações de Pi
pi_n = 4 .* m ./ n_vetor;

% Calculando a evolução do erro (diferença absoluta do Pi do computador)
erro = abs(pi - pi_n);

% Plotando a evolução da sucessão e a evolução do erro
figure;

% Gráfico 1: A evolução da sucessão do valor de Pi
subplot(2, 1, 1);
plot(n_vetor, pi_n, 'b');
yline(pi, 'r--', 'Valor Exato de \pi', 'LineWidth', 1.5);
title('Evolução da Sucessão \pi_n');
xlabel('Número de pontos gerados (n)');
ylabel('Valor Calculado');
grid on;

% Gráfico 2: A evolução do erro
subplot(2, 1, 2);
plot(n_vetor, erro, 'k');
title('Evolução do Erro para Valores Crescentes de n');
xlabel('Número de pontos gerados (n)');
ylabel('Erro | \pi - \pi_n |');
grid on;