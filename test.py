import voiceapp_presage
import sys

def main():
    
    app=voiceapp_presage.Predictions()
    print app.GetPredictions(sys.argv[1])

if __name__ == '__main__':
    main()
