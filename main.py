import argparse
import src.ImageSplitter as ImageSplitter
import src.PrinterPaper as PrinterPaper
import PIL.Image as Image

def main(args):
    img = Image.open(args['f'])

    dpi = (args['dpi'],args['dpi'])
    
    paper = PrinterPaper.PrinterPaper(args['paperwidth'],args['paperheight'],dpi)
    splits = ImageSplitter.split_image(img,args['columns'],args['rows'])

    pdf = []
    for v in [paper.fill_image(v) for v in splits]:
        base = Image.new("RGB",v.size,"WHITE")
        base.paste(v,(0,0),mask=v.getchannel('A'))
        pdf.append(base)
    
    with args['output'] as f:
        pdf[0].save(f,save_all=True, append_images=pdf[1:], dpi = dpi)
    args['f'].close()
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Split image into n*k images and serve as a printable PDF.")
    parser.add_argument('f',metavar='Image', type=argparse.FileType('rb'), help="Path to image to process.")
    parser.add_argument('-n', '--columns', type=int, help="Number of columns.",default=3)
    parser.add_argument('-k', '--rows', type=int, help="Number of rows.", default=3)
    parser.add_argument('-d','--dpi',type=float,help="DPI.",default=300)
    parser.add_argument('-w','--paperwidth',type=float,help="Specify Paper Width in inches.",default=8.5)
    parser.add_argument('-y','--paperheight',type=float,help="Specify Paper Height in inches.",default=11)
    parser.add_argument('-o','--output',type=argparse.FileType('wb'), help="Output file",default=open("out.pdf","wb"))
    args = parser.parse_args()
    main(vars(args))