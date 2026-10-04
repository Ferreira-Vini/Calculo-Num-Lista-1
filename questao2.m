% 1. Criando 401 pontos no intervalo pedido
x = linspace(1 - 2e-8, 1 + 2e-8, 401);

% 2. Calculando a função do jeito que está na lista (Expandida)
% O ponto (.) é necessário para fazer a conta elemento por elemento do vetor
f_expandida = x.^7 - 7.*x.^6 + 21.*x.^5 - 35.*x.^4 + 35.*x.^3 - 21.*x.^2 + 7.*x - 1;

% 3. Calculando a função fatorada: (x - 1)^7
f_fatorada = (x - 1).^7;

% 4. Criando a janela com os gráficos
figure;

% Gráfico 1 (em cima)
subplot(2, 1, 1);
plot(x, f_expandida, 'b', 'LineWidth', 1.5);
title('Função Expandida: f(x) = x^7 - 7x^6 + 21x^5...');
xlabel('Eixo X');
ylabel('f(x)');
grid on;

% Gráfico 2 (embaixo)
subplot(2, 1, 2);
plot(x, f_fatorada, 'r', 'LineWidth', 1.5);
title('Função Fatorada: f(x) = (x - 1)^7');
xlabel('Eixo X');
ylabel('f(x)');
grid on;