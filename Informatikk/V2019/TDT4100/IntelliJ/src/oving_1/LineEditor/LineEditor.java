package oving_1.LineEditor;

import javax.sound.sampled.Line;

public class LineEditor {
    private String text;
    private int insertionIndex;

    public LineEditor(String text, int insertionIndex){
        this.text = text;
        this.insertionIndex = insertionIndex;
    }

    public void left(){
        insertionIndex--;
    }

    public void right(){
        insertionIndex++;
    }

    public void insertString(String s) {
        String leftSub = text.substring(0, insertionIndex);
        String rightSub = text.substring(insertionIndex + 1);

        text = leftSub + s + rightSub;
    }


    public void deleteLeft(){
        text = text.substring(0, insertionIndex-1) + text.substring(insertionIndex);
    }

    public void deleteRight(){
        text = text.substring(0, insertionIndex) + text.substring(insertionIndex+1);
    }

    public String getText(){
        return text;
    }

    public void setText(String s){
        text = s;
    }

    public int getInsertionIndex(){
        return insertionIndex;
    }

    public void setInsertionIndex(int i){
        insertionIndex = i;
    }

    @Override
    public String toString() {
        return text.substring(0, insertionIndex) + "|" + text.substring(insertionIndex);
    }

    public static void main(String args[]){
        LineEditor e = new LineEditor("Hei", 2);
        System.out.println(e);
    }
}

