function [AverageUpdate] = PLA(TrainDataFileName, Iter)
    %Read Data
    DataStr = importdata(TrainDataFileName);
    N = size(DataStr, 1);
    Data = [];
    for i = 1:N
        tempstr = cell2mat(DataStr(i));
        temp = [double(1), str2num(tempstr)];
        Data = [Data;temp];
    end
    Dim = size(Data, 2);
    Dim = Dim-1;
    DataX = Data(:, 1:Dim);
    DataY = Data(:, Dim+1);
    
    %PLA
    UpdateTrack = [];
    for iteration = 1:Iter
        Success = false;
        Weight = zeros(1, Dim, 'double');
        Cycle = randperm(N);
        ID = 1;
        LastFail = -1;
        UpdateCount = 0;
        while ~Success
            CurrentPosition = Cycle(ID);
            CurrentDataX = DataX(CurrentPosition, :);
            CurrentDataY = DataY(CurrentPosition);
            if CurrentDataY*(Weight*CurrentDataX') > 0
                if LastFail == -1 && CurrentID == N
                    Success = true;
                    continue;
                end
                if LastFail == CurrentPosition
                    Success = true;
                    continue;
                end
                ID = GoNext(ID, N);

            else
                LastFail = CurrentPosition;
                Weight = Weight + DataY(CurrentPosition)*DataX(CurrentPosition, :);
                UpdateCount = UpdateCount+1;
                ID = GoNext(ID, N);
                continue;
            end
        end
        UpdateTrack = [UpdateTrack, UpdateCount];
    end
    sort(UpdateTrack)
    histogram(UpdateTrack)
    AverageUpdate = mean(UpdateTrack)
    
function NextID = GoNext(ID, N)
    ID = ID+1;
    if ID > N
        ID = 1;
    end
    NextID = ID;