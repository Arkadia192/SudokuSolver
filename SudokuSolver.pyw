import tkinter as tk
import time
import random

"""
    Berk Öztaş
    27.01.2019
    Enjoy
"""

class SudokuSolver(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.title("Sudoku Solver v.3.9")
        self.master.bind('<Key>', lambda e: self.keyPressed(e))
        self.pack()


        self.possibleBoards = [ "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
                                "400000805030000000000700000020000060000080400000010000000603070500200000104000000",
                                "520006000000000701300000000000400800600000050000000000041800000000030020008700000",
                                "600000803040700000000000000000504070300200000106000000020000050000080600000010000",
                                "480300000000000071020000000705000060000200800000000000001076000300000400000050000",
                                "000014000030000200070000000000900030601000000000000080200000104000050600000708000",
                                "000000520080400000030009000501000600200700000000300000600010000000000704000000030",
                                "602050000000003040000000000430008000010000200000000700500270000000000081000600000",
                                "052400000000070100000000000000802000300000600090500000106030000000000089700000000",
                                "602050000000004030000000000430008000010000200000000700500270000000000081000600000",
                                "092300000000080100000000000107040000000000065800000000060502000400000700000900000",
                                "600302000050000010000000000702600000000000054300000000080150000000040200000000700",
                                "060501090100090053900007000040800070000000508081705030000050200000000000076008000",
                                "005000987040050001007000000200048000090100000600200000300600200000009070000000500",
                                "306070000000000051800000000010405000700000600000200000020000040000080300000500000",
                                "100000308070400000000000000203010000000000095800000000050600070000080200040000000",
                                "600302000040000010000000000702600000000000054300000000080150000000040200000000700",
                                "000030090000200001050900000000000000102080406080500020075000000401006003000004060",
                                "450000030000801000090000000000050090200700000800000000010040000000000702000600800",
                                "023700006800060590900000700000040970307096002000000000500470000000002000080000000",
                                "008400030000300000900001574790008000000007005140000020009060002050000400000090056",
                                "098010000200000060000000000000302050084000000000600000000040809300500000000000100",
                                "002470058000000000000001040000020009528090400009000100000000030300007500685002000",
                                "400000805030000000000700000020000060000050400000010000000603070500200000109000000",
                                "020300000063000005800000001500009030000700000000100008087900260000006070006007004",
                                "100000709040007200800000000070010060300000005060040020000000008005300070702000046",
                                "400000300000802000000700000000100087340000000600000000500060000000010400082000000",
                                "000000071020800000000403000700060050000200300900000000600070000080000400000050000",
                                "600302000040000080000000000702600000000000054300000000080150000000080200000000700",
                                "047080001000000000000600700600003570000005000010060000280040000090100040000020690",
                                "000000801700200000000506000000700050010000300080000000500000020040080000600030000",
                                "380600000009000000020030510000005000030010060000400000017050080000000900000007032",
                                "000500000000000506970000020004802000250100030080030000000004070013050090020003100",
                                "020000000305062009068000300050000000000640802004700900003000001000006000170430000",
                                "080040000300000010000000020005000406900100800200000000000309000060000500000200000",
                                "008090100060500020000006000030107050000000009004000300050000200070003080200700004",
                                "400000508030000000000700000020000060000050800000010000000603070500200000108000000",
                                "100000308060400000000000000203010000000000095800000000050600070000080200040000000",
                                "100006080064000000000040007000090600070400500500070100050000320300008000400000000",
                                "249060003030000200800000005000006000000200000010040820090500700004000001070003000",
                                "000800009087300040600700000008500970000000000043007500000003000030001450400002001",
                                "000501000090000800060000000401000000000070090000000030800000105000200400000360000",
                                "000000801600200000000705000000600020010000300080000000200000070030080000500040000",
                                "047600050803000002000009000000805006000100000602400000078000510006000040090004007",
                                "000007095000001000860020000020073008500000060003004900305000417240000000000000000",
                                "040500000800090030076020000014600000000009007000003600001004050060000003007100200",
                                "083400000000070050000000000040108000000000027000300000206050000500000800000000100",
                                "009000003000009000700000506006500400000300000028000000300750600600000000000120308",
                                "026039000000600001900000700000004009050000200008500000300200900400007620000000004",
                                "203080000800700000000000100060507000400000030000100000000000082050000600010000000",
                                "600302000010000050000000000702600000000000084300000000080150000000080200000000700",
                                "100000900064001070070040000000300000308900500007000020000060709000004010000129030",
                                "000000000900000084062300050000600045300010006000900070000100000405002000030800009",
                                "020000593800500460940060008002030000060080730700200000000040380070000600000000005",
                                "904005000250600100310000008070009000400260000001470000700000002000300806040000090",
                                "000520000090003004000000700010000040080045300600010008702000000008000032040080010",
                                "530020900024030050009000000000010827000700000000098100000000000006400009102050430",
                                "100007860007008010800200009000000002400010000009005000608000000000050900000009304",
                                "000050001100000070060000080000004000009010300000596020080062007007000000305070200",
                                "047020000800001000030000902000005000600810050000040000070000304000900010400270800",
                                "000000940000090005300005070080400100463000000000007080800700000700000028050260000",
                                "020000006000041000007800001000000700003700000600412000010074005008050070000003900",
                                "100000308060400000000000000203010000000000075800000000070500060000080200040000000",
                                "200001090010030700900800020000000850060400000000070003020300060000500000109000205",
                                "007008000006020300030000009010050060000010000070900002000000004083004000260000510",
                                "000360000850000000904008000000006800000000017009004500010500060400009002000003000",
                                "340600000007000000020080570000005000070010020000400000036020010000000900000007082",
                                "000000401800200000000607000000800060040000300010000000600000020050010000700030000",
                                "040050067000100040000200000100800300000000200060000000000040050300000800200000000",
                                "000000040002004001070050090003007000040060000600100800020000100850900060000080003",
                                "800700004050000600000000000030970008000043005000020900006000000200060007071008302",
                                "080004050000700300000000000010085000600000200000040000302600000000000041700000000",
                                "000070080006000500020003061010007002008005340200900000002000000580006030400010000",
                                "000000801600200000000705000000600020010000300080000000200000070040080000500030000",
                                "020000000000600003074080000000003002080040010600500000000010780500009000000000040",
                                "052006800000007020000000600004800900200410000001000008006100380000090006300600109",
                                "000010780500009000000000040020000000000600003074080000000003002080040010600500000",
                                "100000003060300700070005001210700090007000000008010020000806400009020060000400000",
                                "400070100001904605000001000000700002002030000847006000014000806020000300600090000",
                                "000000801700200000000506000000700050010000300080000000500000020030080000600040000",
                                "963000000100008000000205000040800000010000700000030025700000030009020407000000900",
                                "150300000070040200004072000008000000000900108010080790000003800000000000600007423",
                                "000000000057240009800009470009003000500900120003010900060000250000560000070000006",
                                "000075000010020000040003000500000302000800010000000600000100480200000000700000000",
                                "600000703040800000000000000000504080700200000103000000020000050000070900000010000",
                                "000060004006030000100400507700000805000800000608000090002090000400003200009700100",
                                "032000005800300000904280001000400039000600050000010000020006708000004000095000060",
                                "000503000000060700508000016360020000000401000000030005670000208004070000000200500",
                                "050307040100000000030000000508030610000800509060010000000040006000692700002000900",
                                "005008001800000090000000780000400000640000900000053002060000000001380050000907140",
                                "000000000072060100005100082080001300400000000037090010000023800504009000000000790",
                                "000658000004000000120000000000009607000300500002080003001900800306000004000047300",
                                "020300000006008090830500000000200080709005000000006004000000010001000402200700809",
                                "050090000100000600000308000008040009514000000030000200000000004080006007700150060",
                                "000002000000070001700300090800700000020890600013006000090050824000008910000000000",
                                "300080000000700005100000000000000360002004000070000000000060130045200000000000800",
                                "010020300004005060070000008006900070000100002030048000500006040000800106008000000",
                                "000943000060010050000000000800000003750060014100000009000000000020050080000374000",
                                "000651000040020080000000000700000009120030045800000001000000000030040020000719000",
                                "000758000040060010000000000700000008120030045600000009000000000030010090000826000",
                                "000716000030050020000000000700000006120030045500000001000000000090040080000182000",
                                "000012300000400000105006200306000020200070008080000107001500403000001000003740000",
                                "000034500000600000108009700309000070700080005050000108001400203000008000004290000",
                                "000061700000500000406007300302000050500080001070000902009600408000009000003870000",
                                "000091400000700000503004900704000050900020001020000604006300507000006000007810000",
                                "000075100000100000906004700401000020500030006060000403007800602000007000002560000",
                                "000034700000500000304008200208000040900050006070000908009700601000009000005610000",
                                "009370000002000000004000567000402009600090002900806000586000200000000400000087900",
                                "008700050003608007710200000974000080000000000030000924000005092600103400040006100",
                                "001200030004506007350800000542000060000000000070000924000008056400601800080005200",
                                "001200030002401005640300000716000040000000000020000861000003078300804100090005300",
                                "008100020002603007760200000579000010000000000030000976000005091900702400040006500",
                                "009500030004201006560700000453000080000000000070000495000002051100905300030007900",
                                "002700050007608001810300000971000080000000000030000914000005032700103600040006100",
                                "090000040230000065000203000006472900000806000007359600000508000850000039060000010",
                                "010000020230000045000201000006752800000906000009184600000405000590000013060000080",
                                "010000020230000045000602000007864300000907000004253700000406000940000083070000010",
                                "010000020230000045000203000003572400000806000007349600000905000850000039040000010",
                                "010000020340000056000306000007582300000407000008693500000204000250000039070000010",
                                "010000020340000056000504000002675800000201000007438200000306000560000037020000080",
                                "000000000001203400020010050050000040003060200070000080080050070006709300000000000",
                                "000000000006703400020010090010000060004050700070000040090020010007604300000000000",
                                "000000000001403500050060070070000010003080200090000050010090060002105400000000000",
                                "000000000050723090001000200030906070040000060010408050007000500020139040000000000",
                                "000000000010234050003000600060501020020000040070408090001000400050396010000000000",
                                "000000000010234050006000100070408090050000060030902040005000300040615070000000000",
                                "000000000005472800020803070094000210030000050081000630040706020003298100000000000",
                                "000000000060203040000156000047000180005070600028000350000682000030704060000000000",
                                "000000000008070300040301090009030600010267080004050200020804060005090800000000000",
                                "060000020003000400000107000004050800020000070005090300000203000009000500070000060",
                                "010000090003000200000507000004010800090000050008060300000203000009000100050000060"]


        self.boardText = random.choice(self.possibleBoards)
        self.boardState = None

        self.setBoardState()

        self.moveKeys = ["Up", "Right", "Down", "Left"]

        self.count = 0
        self.backtracks = 0

        self.labelstring = tk.StringVar()
        self.labelstring.set("Hiçbir kutu seçilmedi!")

        self.IntervalVal = tk.StringVar()
        self.IntervalVal.set("0.00")

        self.drawEnable = tk.IntVar()
        
        #Was a thing before keyboard controls
        self.isHighlight = True
        self.highlightedElem = "0,0"

        self.selectedBox = None

        self.defColor = "thistle2"
        self.activeColor = "thistle3"
        self.highlightColor = "royal blue"
        self.backgroundColor = "sky blue"

        self.initUI()

    def initUI(self):
        self.boardCanv = tk.Canvas(self, width=600, height=600, background="gray90")
        self.boardCanv.pack(side="left", expand=1)

        self.initBoard()

        self.nameLab = tk.Label(self, text="Berk Öztaş\n27.01.2019\nNot finished")
        self.nameLab.pack(side="top")
        
        
        self.timerFrame = tk.Frame(self, width=100, height=200, background=self.backgroundColor)
        self.timerFrame.pack(side="top", expand=1, padx=2, pady=10)

        self.timelabel = tk.Label(self.timerFrame, background=self.backgroundColor, width=100, height=1, text="Adımlar arası bekleme süresi (sn)")
        self.timelabel.pack(side="top", expand=1, padx=1, pady=5)

        self.timeInterval = tk.Entry(self.timerFrame, width=15, textvariable=self.IntervalVal, state=tk.DISABLED)
        self.timeInterval.pack(side="left", padx=1, pady=5)

        self.timeIntervalUp = tk.Button(self.timerFrame, width=5, height=1, text="Arttır", command=lambda: self.SetWaitingTime("Up"))
        self.timeIntervalUp.pack(side="left", padx=1, pady=5)
        
        self.timeIntervalUp = tk.Button(self.timerFrame, width=5, height=1, text="Azalt", command=lambda: self.SetWaitingTime("Down"))
        self.timeIntervalUp.pack(side="left", padx=1, pady=5)

        self.drawEnableBox = tk.Checkbutton(self, text="Her adımda gösterme (hızlı)", variable=self.drawEnable)
        self.drawEnableBox.pack(side="top", padx=1, pady=1)

        self.buttonFrame = tk.Frame(self, width=100, height=400, background=self.backgroundColor)
        self.buttonFrame.pack(side="top", expand=1, padx=2, pady=5)

        self.hi_there = tk.Button(self.buttonFrame, width=100, height=2, text="Başla", command=self.mainEntry)
        self.hi_there.pack(side="top", pady=10)

        self.defaulter = tk.Button(self.buttonFrame, width=100, height=2, text="Rastgele", command=self.rastgele)
        self.defaulter.pack(side="top", pady=10)

        self.clearer = tk.Button(self.buttonFrame, width=100, height=2, text="Sıfırla", command=self.clearBoard)
        self.clearer.pack(side="top", pady=10)

        """
        self.testBut = tk.Button(self.buttonFrame, width=100, height=2, text="CHANGE", command=lambda: self.changeBoxtext(self.highlightedElem, self.inputBox.get()))
        self.testBut.pack(side="top", pady=10)
        """
        self.label = tk.Label(self.buttonFrame, textvariable=self.labelstring)
        self.label.pack(side="top")
        """
        self.inputBox = tk.Entry(self.buttonFrame)
        self.inputBox.pack(side="top", pady=5)
        """
        self.quit = tk.Button(self.buttonFrame, text="ÇIKIŞ", width=100, height=2, fg="red", command=self.master.destroy)
        self.quit.pack(side="top", pady=10)

        self.log = tk.Text(self.buttonFrame, width=90, height=10)
        self.log.pack(side="top", pady=10)

        self.log.insert(0.0, "Ok tuşlarıyla veya \ntıklayarak kutu seçip\nKlavyedeki sayılarla\ndeğerleri\ndeğiştirebilirsiniz\nBoş kutu == 0")

        self.boardCanv.tag_bind("box", "<1>", self.clickedBox)

    def rastgele(self):
        self.boardText = random.choice(self.possibleBoards)
        self.defaultBoard()

    def defaultBoard(self):
        self.boardState = []
        count = 0
        for row in range(9):
            self.boardState.append([])
            for column in range(9):
                self.boardState[row].append(self.boardText[count])
                self.changeBoxtext(str(row)+","+str(column), self.boardText[count])
                count += 1


    def clearBoard(self):
        for i in range(9):
            for j in range(9):
                self.changeBoxtext(str(i)+","+str(j), "0")
                self.boardState[i][j] = "0"

    def initBoard(self):
        if self.boardState == None:
            self.boardState = []
            for i in range(9):
                self.boardState.append([])
                for j in range(9):
                    self.boardState[i].append("0")

        self.SIDE = 65
        self.ENDLEN = 585
        self.MARGIN = 2

        for i in range(9):
            for j in range(9):
                bbox = (self.MARGIN+1+i*self.SIDE, self.MARGIN+1+j*self.SIDE, self.MARGIN+1+(i+1)*self.SIDE, self.MARGIN+1+(j+1)*self.SIDE)
                self.boardCanv.create_rectangle(bbox, fill=self.defColor, activefill=self.activeColor, tags=("box", "b"+str(j)+","+str(i)))

        #LINES
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = self.MARGIN + i * self.SIDE
            y0 = self.MARGIN + 0
            x1 = self.MARGIN + i * self.SIDE
            y1 = self.ENDLEN - self.MARGIN
            self.boardCanv.create_line(x0, y0, x1, y1, fill=color)
            x0 = self.MARGIN + 0
            y0 = self.MARGIN + i * self.SIDE
            x1 = self.ENDLEN - self.MARGIN
            y1 = self.MARGIN + i * self.SIDE
            self.boardCanv.create_line(x0, y0, x1, y1, fill=color)

        self.updateText()


    def setBoardState(self):
        self.boardState = []
        
        count = 0

        for row in range(9):
            self.boardState.append([])
            for column in range(9):
                self.boardState[row].append(self.boardText[count])
                count += 1

    def SetWaitingTime(self, UorD):

        InterVal = float(self.IntervalVal.get())
        if UorD == "Up":
            InterVal += 0.01
        elif UorD == "Down":
            InterVal -= 0.01
            if InterVal < 0:
                InterVal = 0.00
        InterVal = round(InterVal, 2)
        self.IntervalVal.set(str(InterVal))

    def changeBoxtext(self, id, to):
        try:
            to = int(to)
        except ValueError:
            return None
        if int(to) < 0 or int(to) > 9:
            return None
        if str(to) == "0":
            self.boardCanv.itemconfig(self.boardCanv.find_withtag(id), text=" ")
        else:
            self.boardCanv.itemconfig(self.boardCanv.find_withtag(id), text=to)

    def keyPressed(self, key):
        if key.keysym in self.moveKeys:
            x = int(self.highlightedElem.split(",")[0])
            y = int(self.highlightedElem.split(",")[1])
            if key.keysym == "Up":
                x = 8 if x == 0 else x-1
            elif key.keysym == "Down":
                x = 0 if x == 8 else x+1
            elif key.keysym == "Right":
                y = 0 if y == 8 else y+1
            elif key.keysym == "Left":
                y = 8 if y == 0 else y-1

            self.highlightGridElem(x, y)

        elif key.keysym == "Escape":
            self.master.destroy()

        else:
            try:
                val = int(key.keysym)
                if self.isHighlight:
                    self.changeBoxtext(self.highlightedElem, key.keysym)
                    a, b = int(self.highlightedElem.split(",")[0]), int(self.highlightedElem.split(",")[1])
                    self.boardState[a][b] = str(val)
            except ValueError:
                pass

    def mainRoutine(self, row, column, theMove):
        self.boardState[row][column] = str(theMove)
        if not (self.drawEnable.get() == 1):
            self.highlightGridElem(row, column)
            self.changeBoxtext(str(row)+","+str(column), str(theMove))
            self.master.update()
            time.sleep(float(self.IntervalVal.get()))   
        if self.backtracks % 2000 == 0:
            self.updateText()
            self.master.update()

    def mainEntry(self):

        self.defaulter["state"] = "disabled"
        self.clearer["state"] = "disabled"

        self.main()

        self.updateText()
        
        self.defaulter["state"] = "normal"
        self.clearer["state"] = "normal"

    def main(self):
        if self.boardText == None:
            print("Please set a board using .setBoard()")
            return False
        for row in range(9):
            for column in range(9):
                if self.boardState[row][column] == "0":
                    for i in range(1, 10):
                        theMove = str(i)
                        if self.isMoveValid(theMove, row, column) == True:
                            self.mainRoutine(row, column, str(theMove))
                            
                            if not self.main():
                                self.backtracks += 1
                                self.mainRoutine(row, column, "0")
                                self.log.insert(0.0, str(self.backtracks)+"\n")
                            
                    for i in range(9):
                        for j in range(9):
                            if self.boardState[i][j] == "0":
                                return False
        self.backtracks = 0
        return True        


    def isMoveValid(self, move, moveRow, moveCol):
        if self.boardState[moveRow][moveCol] != "0":
            return None
        self.boardState[moveRow][moveCol] = move
        toReturn = self.isBoardValid()
        self.boardState[moveRow][moveCol] = "0"
        return toReturn


    def isBoardValid(self):
        rowHas = ""
        columnHas = ["", "", "", "", "", "", "", "", ""]
        blockHas = [["", "", ""], 
                    ["", "", ""], 
                    ["", "", ""]]

        for row in range(9):
            rowHas = ""
            for column in range(9):
                toAdd = self.boardState[row][column]

                if toAdd != "0":
                    if toAdd in rowHas:
                        return False
                    elif toAdd in columnHas[column]: 
                        return False
                    elif toAdd in blockHas[int(row/3)][int(column/3)]: 
                        return False

                rowHas += toAdd
                columnHas[column] += toAdd
                blockHas[int(row/3)][int(column/3)] += toAdd

        return True


    def highlightGridElem(self, row, col):
        if self.isHighlight:
            x,y = self.highlightedElem.split(",")[0], self.highlightedElem.split(",")[1]
            self.deHighlightGridElem(x, y)
        else:
            self.isHighlight = True
        self.boardCanv.itemconfig(self.getGridElem(row, col, True), fill=self.highlightColor)
        self.highlightedElem = str(row)+","+str(col)
        self.labelstring.set(str(int(row)+1)+","+str(int(col)+1) + " noktası seçildi.")
        #self.labelstring.set("Selected box at: " + str(row)+","+str(col))

    def deHighlightGridElem(self, row, col):
        self.boardCanv.itemconfig(self.getGridElem(row, col, True), fill=self.defColor)

    def getGridElem(self, row, col, box=False):
        if box:
            return self.boardCanv.find_withtag("b"+str(row)+","+str(col))
        return self.boardCanv.find_withtag(str(row)+","+str(col))

    def updateText(self):
        leftBase = self.MARGIN + int(self.SIDE/2)
        for i in range(9):
            for j in range(9):
                self.boardCanv.delete(self.getGridElem(i, j))
                if self.boardState[i][j] == "0":
                    self.boardCanv.create_text((leftBase+self.SIDE*j, leftBase+self.SIDE*i), text=" ", font=("Helvetica", 15), fill="black", state=tk.DISABLED, tags=(str(i)+","+str(j)))
                else:
                    self.boardCanv.create_text((leftBase+self.SIDE*j, leftBase+self.SIDE*i), text=self.boardState[i][j], font=("Helvetica", 15), fill="black", state=tk.DISABLED, tags=(str(i)+","+str(j)))

    def clickedBox(self, event):
        item = self.boardCanv.find_closest(event.x, event.y)
        if "box" in self.boardCanv.gettags(item):
            loc = self.boardCanv.gettags(item)[1][1:].split(",")
            self.highlightGridElem(loc[0], loc[1])
            

    def say_hi(self):
        self.count += 1
        self.log.insert(0.0, str(self.count)+"\n")

if __name__ == '__main__':
    root = tk.Tk()
    app = SudokuSolver(master=root)
    app.mainloop()