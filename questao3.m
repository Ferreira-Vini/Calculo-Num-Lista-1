% Definir o número de iterações (20 é suficiente para ver o problema)
N = 20;

% Criar um vetor para guardar os valores de I
% (Como o MATLAB não tem índice 0, I_0 será guardado em I(1), I_1 em I(2), etc.)
I = zeros(1, N+1); 

% Valor inicial da sucessão
I(1) = (1/exp(1)) * (exp(1) - 1); 

% Ciclo para calcular a sucessão
for n = 0:N-1
    % A fórmula é I_{n+1} = 1 - (n+1)*I_n
    I(n+2) = 1 - (n + 1) * I(n+1);
end

% Vetor com os valores de n (de 0 a N) para o eixo X do gráfico
n_vals = 0:N;

% Mostrar os valores na Command Window
disp('Valores calculados de I_n:');
disp([n_vals' I']);

% Criar o gráfico
figure;
plot(n_vals, I, '-o', 'LineWidth', 1.5, 'MarkerFaceColor', 'b');
title('Evolução da Sucessão I_n');
xlabel('n');
ylabel('Valor de I_n');
grid on;