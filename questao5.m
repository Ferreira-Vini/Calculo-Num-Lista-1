% Valores de referência exigidos pela questão
pi_alvo = 3.141592;
precisao = 1e-4;

% Inicializando variáveis
n = 0;
erro = 1; % Começamos com um erro maior que a precisão para o ciclo rodar

% Ciclo while: repete até o erro atingir a precisão desejada
while erro > precisao
    % Chama a função que criamos lá embaixo para o 'n' atual
    pi_calculado = calcula_pi_serie(n);

    % Calcula o erro absoluto
    erro = abs(pi_alvo - pi_calculado);

    % Se o erro ainda for maior que 10^-4, incrementamos n para tentar de novo
    if erro > precisao
        n = n + 1;
    end
end

% Imprime os resultados na Command Window
disp('--- Resultado da Aproximação de Pi ---');
disp(['Valor de n necessário: ', num2str(n)]);
disp(['Valor Calculado: ', num2str(pi_calculado)]);
disp(['Erro Absoluto Final: ', num2str(erro)]);

% =========================================================================
% FUNÇÃO PARA CALCULAR A SOMA PARCIAL
% =========================================================================
function pi_aprox = calcula_pi_serie(n)
pi_aprox = 0; % Começa a soma do zero
% Somatório de m = 0 até n
for m = 0:n
    % A fórmula exata da série fornecida na questão
    termo = (16^-m) * (4/(8*m + 1) - 2/(8*m + 4) - 1/(8*m + 5) - 1/(8*m + 6));
    pi_aprox = pi_aprox + termo;
end
end